import numpy as np
from cli.allowed_args import assert_only_allowed_args
from img_transformations.colors import bw_to_set, set_to_bw

i = np.array([[1, 1]]).T
iii = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]).T


def dilation(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--element'])
    A = bw_to_set(arr)
    print(A)

    A += 50

    return set_to_bw(A, arr.shape)

    