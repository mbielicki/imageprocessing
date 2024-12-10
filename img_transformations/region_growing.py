from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg
import numpy as np

from constants import MAX_PIXEL_VALUE
from utils import time_it
import matplotlib.pyplot as plt

@time_it
def region_growing(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--threshold', '--seeds'])
    threshold = get_int_arg(args, '--threshold', default=10, range=(0, 255))
    height, width, colors = arr.shape
    seed_n = get_int_arg(args, '--seeds', default=2, range=(1, width * height))

    seeds = choose_seeds(arr, seed_n)
    map = np.zeros((height, width, 3), dtype=np.uint8)

    for i, seed in enumerate(seeds):
        similar = get_similar(seed, arr, threshold)
        map = fill(map, seed, similar, get_color(i))

    return map

def fill(map: np.ndarray, seed: tuple, similar: np.ndarray, c: np.ndarray):
    stack = [seed]
    while stack:
        p = stack.pop()
        map[p] = c
        for pi in get_neighbors(p, map.shape[0:2]):
            if similar[pi] and np.all(map[pi] == [0, 0, 0]): # if pi is seed, merge regions
                stack.append(pi)

    return map

def get_neighbors(p, shape) -> np.ndarray:
    y, x = p
    height, width = shape
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
    
    
def get_similar(s, arr, threshold):
    return np.all(((arr - threshold < arr[s]) & (arr[s] < arr + threshold)), axis=2)

def choose_seeds(arr, seed_n) -> list:
    height, width, colors = arr.shape
    ns = np.random.randint(0, height * width, seed_n)
    xs = ns % width
    ys = ns // width
    return list(zip(xs, ys))

def get_color(i: int) -> np.ndarray:
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
    return colors[i % len(colors)]