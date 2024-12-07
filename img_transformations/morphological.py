from itertools import product
import numpy as np
from cli.allowed_args import assert_only_allowed_args
from constants import MAX_PIXEL_VALUE
from img_transformations.colors import as_binary, bw_to_indices, indices_to_bw
from utils import time_it

import seaborn as sns # TODO remove
import matplotlib.pyplot as plt

iii_v = product([-1, 0, 1], [-1, 0, 1])
iii_v = np.array(list(iii_v))

# -1 is ignored
iii = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]) 

plus_se = np.array([[-1, 1, -1],
                [ 1, 1,  1],
                [-1, 1, -1]]) 

v   = np.array([[-1, -1, -1],
                [-1,  1,  1],
                [-1,  1, -1]]) 

xii = np.array([[0,   0,   0],
                [-1,  1,  -1],
                [1,   1,   1]])

lse = np.array([[-1, 1, -1],
                [0, 1, -1],
                [1, 1, -1]]) # TODO make se class with center field


def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    arr = arr[:, :, 0]
    A = bw_to_indices(arr)

    P = (A[:, None] + iii_v).reshape((-1, A.shape[1])) 

    return indices_to_bw(P, arr.shape)

def dilate (A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A = bw_to_indices(A)
    B = bw_to_indices(B)
    P = (A[:, None] + B).reshape((-1, A.shape[1]))

    return indices_to_bw(P, A.shape)

def equals_se(window: np.ndarray, se: np.ndarray) -> bool:
    def eq(w: int, k: int) -> bool:
        return k < 0 or (w == k) 
    
    vec_eq = np.frompyfunc(eq, 2, 1)
    
    return (vec_eq(window, se)).all()

def erosion(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = plus_se

    P = erode(A, B) * MAX_PIXEL_VALUE

    return P[:, :, None]

def erode(A: np.ndarray, B: np.ndarray) -> np.ndarray: 
    
    orig_shape = A.shape
    se_size = np.max(B.shape)
    pad_width = se_size // 2

    padded = np.pad(array=A, pad_width=pad_width, mode='constant')

    windows = np.array([
        padded[i:(i + se_size), j:(j + se_size)]
        for i in range(orig_shape[0]) for j in range(orig_shape[1])
    ])

    new_arr = np.array([equals_se(win, B) for win in windows]).reshape(orig_shape)

    return new_arr


def opening(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    return dilation(args, erosion(args, arr))

def closing(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    return erosion(args, dilation(args, arr))

@time_it
def hmt(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = lse
    P = erode(A, B)

    return P[:, :, None] * MAX_PIXEL_VALUE