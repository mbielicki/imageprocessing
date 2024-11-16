import numpy as np

from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg
from utils import clip, time_it


edge_sharpening_kernels = [
    np.array([[0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]]).T,
    np.array([[-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]]).T,
    np.array([[1, -2, 1],
            [-2, 5, -2],
            [1, -2, 1]]).T
]


blur_kernel = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]]).T / 16

@time_it
def edge_sharpening(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--kernel'])

    kernel = get_int_arg(args, '--kernel', range=(0, len(edge_sharpening_kernels) - 1), default=0)

    colors = arr.shape[2]
    
    for c in range(colors):
        if kernel == 0:
            arr[:, :, c] = edge_sharpening_optimized_convolution(arr[:, :, c])
        else:
            arr[:, :, c] = convolution(arr[:, :, c], edge_sharpening_kernels[kernel])


    return arr

def edge_sharpening_optimized_convolution(arr: np.ndarray) -> np.ndarray:
    # Optimized for:
    #    0   -1    0
    #   -1    5   -1
    #    0   -1    0
    
    M = 1

    width = arr.shape[1]
    height = arr.shape[0]

    x = arr.T
    g = x.copy()

    for p in range(M, width - M):
        for q in range(M, height - M):
            val = 5 * x[p, q] - x[p - 1, q] - x[p + 1, q] - x[p, q - 1] - x[p, q + 1]
            g[p, q] = clip(val)

    g = g.T

    return g


def convolution(arr: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    M = (kernel.shape[0] - 1 ) // 2

    width = arr.shape[1]
    height = arr.shape[0]

    x = arr.T
    g = x.copy()

    for p in range(M, width - M):
        for q in range(M, height - M):
            val = (kernel * x[p - M : p + M + 1, q - M : q + M + 1]).sum()
            g[p, q] = clip(val)

    g = g.T

    return g

def orosenfeld(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--P'])

    P = get_int_arg(args, '--P', allowed=[1, 2, 4, 8, 16], default=1)

    colors = arr.shape[2]
    
    for c in range(colors):
        arr[:, :, c] = calculate_rosenfeld(arr[:, :, c], P)

    return arr

def calculate_rosenfeld(arr: np.ndarray[np.uint8, np.uint8], P) -> np.ndarray:
    # Assumes one color
    # Rosenfeld operator:
    # gP(n,m) = 1/P * [x(n+P−1,m) + x(n+P−2,m) + … + x(n,m) − x(n−1,m) − x(n−2,m) − … − x(n−P,m)],
    # where P = 1,2,4,8,16,….

    height = arr.shape[0]
    width = arr.shape[1]

    x = arr.T
    g = x.copy()

    for n in range(P, width - P + 1):
        for m in range(height):
            sum = 0

            for n_shift in range(-P, P):
                if n_shift >= 0:
                    sum += x[n + n_shift, m]
                else:
                    sum -= x[n + n_shift, m]

            g[n, m] = sum / P

    g = g.T

    return g