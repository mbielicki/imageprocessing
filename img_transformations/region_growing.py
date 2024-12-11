from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg
import numpy as np

from constants import MAX_PIXEL_VALUE
from utils import time_it
import matplotlib.pyplot as plt

class Region:
    def __init__(self, seed: tuple, color: tuple, arr: np.ndarray, map: np.ndarray, threshold: int):
        self.seed = seed
        self.color = color
        self.done = False
        self.mean = arr[seed]
        self.size = 1

        self.map = map
        self.arr = arr
        self.regions = []

        self.threshold = threshold

        self.queue = [seed]
    
    def add_to_mean(self, v: np.ndarray):
        self.size += 1
        self.mean = self.mean + v / (self.size)
    
    def grow(self):
        next_queue = []
        while self.queue:
            p = self.queue.pop(0)
            if self.is_similar(self.arr[p]):
                if self._is_0(p):
                    self.add_to_mean(self.arr[p])
                    self.map[p] = self.color
                    for pi in get_neighbors(p, self.map.shape):
                        next_queue.append(pi)
                elif self._is_already_in(p):
                    continue
                else: # is in other region
                    r = self._get_region_whose_seed_is(p)
                    if r is not None:
                        self.merge(r)

        if not next_queue:
            self.done = True
        self.queue = next_queue
        return self.map
    
    def is_similar(self, val) -> bool:
        val = np.array(val)
        if np.all(val - self.threshold < self.mean) and np.all(self.mean < val + self.threshold):
            return True

    def _is_0(self, p):
        return np.all(self.map[p] == 0)
    
    def _is_already_in(self, p):
        return np.all(self.map[p] == self.color)
    
    def _get_region_whose_seed_is(self, p):
        for r in self.regions:
            if r.seed == p:
                return r
            
    def merge(self, r: 'Region'):
        self.mean = (self.mean * self.size + r.mean * r.size) / (self.size + r.size)
        self.size += r.size
        r.done = True
        return np.where(self.map == r.color, self.color, self.map)

@time_it
def region_growing(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--threshold', '--seeds'])
    threshold = get_int_arg(args, '--threshold', default=10, range=(0, 255))
    height, width, colors = arr.shape
    seed_n = get_int_arg(args, '--seeds', default=2, range=(1, width * height))

    map = np.zeros((height, width, 3), dtype=np.uint8)
    regions = choose_seeds(arr, seed_n, map, threshold)

    for region in regions:
        region.regions = regions
        while not region.done:
            map = region.grow()


    # while regions:
    #     region = regions.pop(0)
    #     map = region.grow()
    #     if not region.done:
    #         map = region.grow()
    #         regions.append(region)

    return map

def get_neighbors(p, shape) -> np.ndarray:
    y, x = p
    height, width, _ = shape
    potential_neighbors = [(y, x+1), 
                 (y, x-1),
                 (y+1, x),
                 (y-1, x)]
    res = list()
    for n in potential_neighbors:
        n_y, n_x = n
        if 0 <= n_y and n_y < height and 0 <= n_x and n_x < width:
            res.append(n)

    return res
    
    


def choose_seeds(arr: np.ndarray, seed_n: int, map, threshold) -> list[Region]:
    height, width, colors = arr.shape
    ns = np.random.randint(0, height * width, seed_n)
    xs = ns % width
    ys = ns // width
    return [Region((ys[i], xs[i]), get_color(i), arr, map, threshold) 
            for i in range(seed_n)]

colors = np.array([
        [158, 1, 66],
        [213, 62, 79],
        [244, 109, 67],
        [253, 174, 97],
        [254, 224, 139],
        [255, 255, 191],
        [230, 245, 152],
        [171, 221, 164],
        [102, 194, 165],
        [50, 136, 189],
        [94, 79, 162],
    ])
def get_color(i: int) -> np.ndarray:
    return (colors[i % len(colors)] + i * 20) % MAX_PIXEL_VALUE