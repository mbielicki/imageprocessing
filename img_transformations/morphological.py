import numpy as np
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_point_arg
from constants import DEBUG_MODE, MAX_PIXEL_VALUE
from img_transformations.colors import as_binary, as_bw, bw_to_indices, indices_to_bw
from utils import time_it

import seaborn as sns
import matplotlib.pyplot as plt
import structural_elements as se

def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = se.plus
    P = dilate(A, B)

    return as_bw(P)

def erosion(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se'])
    A = as_binary(arr)
    B = se.plus

    P = erode(A, B)

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

def points_in_set(points: np.ndarray, set: np.ndarray) -> np.ndarray:
    return (points[:, None, :] == set).all(axis=2).any(axis=1)

def sets_equal(A: np.ndarray, B: np.ndarray) -> bool:
    m = (A[:, None, :] == B).all(axis=2)
    return m.any(axis=1).all() and m.any(axis=0).all()

@time_it
def m3(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--se', '--p'])
    A = as_binary(arr)
    shape = A.shape
    Ai = bw_to_indices(A)
    B = se.iii
    p = get_point_arg(args, '--p', default='0,0', range=((0, 0), shape))
    X = np.array([p])

    i = 0
    while True:
        dilated_X = dilate_set(X, B)
        Xk = dilated_X[points_in_set(dilated_X, Ai)]
        if DEBUG_MODE: 
            print(f'iteration {i}, size: {Xk.shape[0]} / {shape[0] * shape[1]}', end='\r')
            i += 1
        if sets_equal(Xk, X): break
        X = Xk

    return indices_to_bw(X, shape)[:, :, None] * MAX_PIXEL_VALUE

def dilate_set(Ai: np.ndarray, B: se.StructuralElement) -> np.ndarray:
    dilated = (Ai[:, None] + B.indices).reshape((-1, Ai.shape[1]))
    return np.unique(dilated, axis=0)

def dilate(A: np.ndarray, B: se.StructuralElement, pad_val: int = 0) -> np.ndarray:
    shape = A.shape
    pad_width = B.max()
    A = np.pad(A, pad_width=pad_width, mode='constant', constant_values=pad_val)
    
    Ai = bw_to_indices(A)
    P = dilate_set(Ai, B)

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