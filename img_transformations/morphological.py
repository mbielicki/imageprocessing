from itertools import product
import numpy as np
from cli.allowed_args import assert_only_allowed_args
from constants import MAX_PIXEL_VALUE
from img_transformations.colors import as_binary, as_bw, bw_to_indices, indices_to_bw
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
    A = as_binary(arr)
    P = dilate(A, iii_v)

    return as_bw(P)

def dilate(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    shape = A.shape
    A = bw_to_indices(A)
    P = (A[:, None] + B).reshape((-1, A.shape[1]))

    return indices_to_bw(P, shape)

def equals_se(window: np.ndarray, se: np.ndarray) -> bool:
    def eq(w: int, k: int) -> bool:
        return k < 0 or (w == k) 
    
    vec_eq = np.frompyfunc(eq, 2, 1)
    
    return (vec_eq(window, se)).all()

@time_it
def erosion(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = iii_v

    P = erode(A, B)
    
    B = indices_to_bw(B, (3, 3), offset=(1, 1))
    plot_imgs(A, B, P)

    return P[:, :, None] * MAX_PIXEL_VALUE


def erode(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A = A == 0
    B = -B
    P = dilate(A, B) == 0

    return P


def opening(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    return dilation(args, erosion(args, arr))

def closing(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    return erosion(args, dilation(args, arr))

def hmt(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = lse
    P = erode(A, B)

    return P[:, :, None] * MAX_PIXEL_VALUE

def plot_imgs(A: np.ndarray, B: np.ndarray, P: np.ndarray) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    sns.heatmap(A, ax=ax[0][0])
    sns.heatmap(B, ax=ax[0][1], vmin=-1, vmax=1)
    sns.heatmap(P, ax=ax[1][0])
    plt.tight_layout()
    plt.show()