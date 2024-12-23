import itertools
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg
import numpy as np

from constants import MAX_PIXEL_VALUE
from utils import time_it
import matplotlib.pyplot as plt

class Region:
    def __init__(self, seed: tuple, color: tuple, arr: np.ndarray, map: np.ndarray, n_threshold: int, s_threshold: int):
        self.seed = seed
        self.color = color
        self.done = False
        self.seed_val = arr[seed]
        self.size = 1

        self.map = map
        self.arr = arr
        self.regions = []

        self.n_threshold = n_threshold
        self.s_threshold = s_threshold

        self.queue = [(seed, seed)]
    
    def grow(self):
        next_queue = []
        while self.queue:
            p, initiator = self.queue.pop(0)
            if self.is_similar(self.arr[p], self.arr[initiator]):
                if self._is_0(p):
                    self.map[p] = self.color
                    for pi in get_neighbors(p, self.map.shape):
                        next_queue.append((pi, p))
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
    
    def is_similar(self, val, neighbor_val) -> bool:
        val = np.array(val)
        if self.n_threshold >= MAX_PIXEL_VALUE:
            neighbor_is_similar = True
        else:
            neighbor_is_similar = np.all(val - self.n_threshold < neighbor_val) and np.all(neighbor_val < val + self.n_threshold)
        if self.s_threshold >= MAX_PIXEL_VALUE:
            seed_is_similar = True
        else:
            seed_is_similar = np.all(val - self.s_threshold < self.seed_val) and np.all(self.seed_val < val + self.s_threshold)

        if neighbor_is_similar and seed_is_similar:
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
        r.done = True
        self.queue += r.queue
        return np.where(self.map == r.color, self.color, self.map)

@time_it
def region_growing(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--nthreshold', '--sthreshold', '--seeds'])
    n_threshold = get_int_arg(args, '--nthreshold', default=MAX_PIXEL_VALUE, range=(0, MAX_PIXEL_VALUE))
    s_threshold = get_int_arg(args, '--sthreshold', default=MAX_PIXEL_VALUE, range=(0, MAX_PIXEL_VALUE))

    height, width, colors = arr.shape
    seed_n = get_int_arg(args, '--seeds', default=2, range=(1, width * height))

    map = np.zeros((height, width, 3), dtype=np.uint8)
    regions = choose_seeds(arr, seed_n, map, n_threshold, s_threshold)

    for region in regions:
        region.regions = regions
        while not region.done:
            map = region.grow()

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
    
    


def choose_seeds(arr: np.ndarray, seed_n: int, map, n_threshold, s_threshold) -> list[Region]:
    height, width, colors = arr.shape

    seed_n_y = int(np.sqrt(seed_n * width / height))
    seed_n_x = seed_n // seed_n_y
    space_y = height // seed_n_y
    space_x = width // seed_n_x

    xs = np.linspace(0, width - space_x - 1, seed_n_x, dtype=int) + space_x // 2
    ys = np.linspace(0, height - space_y - 1, seed_n_y, dtype=int) + space_y // 2

    points = itertools.product(ys, xs)

    return [Region(p, get_color(i), arr, map, n_threshold, s_threshold) 
            for i, p in enumerate(points)]

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