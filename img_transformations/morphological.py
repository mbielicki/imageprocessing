import numpy as np
from cli.allowed_args import assert_only_allowed_args
from constants import DEBUG_MODE, MAX_PIXEL_VALUE
from img_transformations.colors import as_binary, as_bw, bw_to_indices, indices_to_bw
from utils import time_it

import seaborn as sns
import matplotlib.pyplot as plt
import structural_elements as se

def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = se.iii
    P = dilate(A, B)

    return as_bw(P)

def erosion(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = se.j

    P = erode(A, B)
    if DEBUG_MODE: plot_imgs(A, B, P)

    return P[:, :, None] * MAX_PIXEL_VALUE

def opening(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    return dilation(args, erosion(args, arr))

def closing(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    return erosion(args, dilation(args, arr))

def hmt(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B1 = se.j
    C1 = erode(A, B1)

    Ac = A == 0
    B2 = B1.set_use(0)
    C2 = erode(Ac, B2)

    P = C1 & C2

    return P[:, :, None] * MAX_PIXEL_VALUE


def dilate(A: np.ndarray, B: se.StructuralElement, pad_val: int = 0) -> np.ndarray:
    shape = A.shape
    pad_width = B.max()
    A = np.pad(A, pad_width=pad_width, mode='constant', constant_values=pad_val)
    
    Ai = bw_to_indices(A)
    P = (Ai[:, None] + B.indices).reshape((-1, Ai.shape[1]))

    return indices_to_bw(P, shape, offset=(pad_width, pad_width))

def erode(A: np.ndarray, B: se.StructuralElement) -> np.ndarray:
    Ac = A == 0
    Br = B.reflect()
    P = dilate(Ac, Br, pad_val=1) == 0

    return P

def plot_imgs(original: np.ndarray, se: se.StructuralElement = None, result: np.ndarray = None) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(7, 6))
    sns.heatmap(original, ax=ax[0][0])
    if se is not None: 
        se = se.copy()
        se.arr = se.arr.astype(np.float32)
        se.arr[se.center] -= 0.15
        sns.heatmap(se.arr, ax=ax[0][1], vmin=-1.0, vmax=1.0)

    if result is not None:
        sns.heatmap(result, ax=ax[1][0])
    plt.tight_layout()
    plt.show()