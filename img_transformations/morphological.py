from itertools import product
import numpy as np
from cli.allowed_args import assert_only_allowed_args
from img_transformations.colors import bw_to_set, set_to_bw
from utils import time_it

iii = product([-1, 0, 1], [-1, 0, 1])
iii = np.array(list(iii))

@time_it
def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--element'])
    A = bw_to_set(arr)

    P = np.array([a + b for a in A for b in iii])

    return set_to_bw(P, arr.shape)

    