from itertools import product
import numpy as np
from cli.allowed_args import assert_only_allowed_args
from constants import MAX_PIXEL_VALUE
from img_transformations.colors import bw_to_indices, indices_to_bw
from utils import time_it

iii_v = product([-1, 0, 1], [-1, 0, 1])
iii_v = np.array(list(iii_v))

iii = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]) 

v   = np.array([[-1, -1, -1],
                [-1,  1,  1],
                [-1,  1, -1]]) 

def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = bw_to_indices(arr)

    P = (A[:, None] + iii_v).reshape((-1, A.shape[1])) 

    return indices_to_bw(P, arr.shape)

def equals_se(window: np.ndarray, se: np.ndarray) -> bool:
    def eq(w: int, k: int) -> bool:
        return k < 0 or (w == k) 
    
    vec_eq = np.frompyfunc(eq, 2, 1)
    
    return (vec_eq(window, se)).all()
@time_it
def erosion(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    arr = arr[:, :, 0]
    
    orig_shape = arr.shape
    se_size = 3
    pad_width = se_size // 2
    se = iii * MAX_PIXEL_VALUE

    padded = np.pad(array=arr, pad_width=pad_width, mode='constant')

    windows = np.array([
        padded[i:(i + se_size), j:(j + se_size)]
        for i in range(orig_shape[0]) for j in range(orig_shape[1])
    ])

    new_arr = np.array([equals_se(win, se) for win in windows]).reshape(orig_shape) * MAX_PIXEL_VALUE

    return new_arr[:, :, None]

def opening(args: dict, arr: np.ndarray) -> np.ndarray:
    return dilation(args, erosion(args, arr))

def closing(args: dict, arr: np.ndarray) -> np.ndarray:
    return erosion(args, dilation(args, arr))