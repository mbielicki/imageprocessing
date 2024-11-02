import numpy as np

from cli.allowed_args import assert_only_allowed_args


edge_sharpening_kernel = np.array([[1, -2, 1],
                                    [-2, 5, -2],
                                    [1, -2, 1]]).T

blur_kernel = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]]).T / 16


def edge_sharpening(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    colors = arr.shape[2]
    
    for c in range(colors):
        arr[:, :, c] = convolution(arr[:, :, c], edge_sharpening_kernel)


    return arr


def convolution(arr: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    M = (kernel.shape[0] - 1 ) // 2

    width = arr.shape[1]
    height = arr.shape[0]

    x = arr.T
    g = x.copy()

    for p in range(M, width - M):
        for q in range(M, height - M):
            g[p, q] = (kernel * x[p - M : p + M + 1, q - M : q + M + 1]).sum()

    g = g.T

    return g