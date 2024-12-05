from itertools import product
import numpy as np
from cli.allowed_args import assert_only_allowed_args
from img_transformations.colors import bw_to_set, set_to_bw
from utils import time_it

iii = product([-1, 0, 1], [-1, 0, 1])
iii = np.array(list(iii))

def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--element'])
    A = bw_to_set(arr)

    P = (A[:, None] + iii).reshape((-1, A.shape[1])) 

    return set_to_bw(P, arr.shape)

def vector_in_set(vector: np.ndarray, set: np.ndarray) -> bool:
    return np.any(np.all(vector == set, axis=1))

@time_it
def erosion(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--element'])
    A = bw_to_set(arr)

    # i_to_delete = []
    # for i, p in enumerate(A):
    #     for b in iii:
    #         if not vector_in_set(p + b, A):
    #             i_to_delete.append(i)
    #             break
                
    # P = np.delete(A, i_to_delete, axis=0)

    
    # mask = [np.all([vector_in_set(p + b, A) for b in iii]) for p in A]
    mask = [
        np.all([
            np.any(np.all(p + b == A, axis=1))
            for b in iii]) for p in A
        ]   
    P = A[mask]


    return set_to_bw(P, arr.shape)