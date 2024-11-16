import numpy as np

from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg
from utils import time_it


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
            g[p, q] = 5 * x[p, q] - x[p - 1, q] - x[p + 1, q] - x[p, q - 1] - x[p, q + 1]

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
            g[p, q] = (kernel * x[p - M : p + M + 1, q - M : q + M + 1]).sum()

    g = g.T

    return g

@time_it
def orosenfeld(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--P'])

    P = get_int_arg(args, '--P', allowed=[1, 2, 4, 8, 16], default=1)

    colors = arr.shape[2]
    width = arr.shape[1]
    height = arr.shape[0]
    
    output_shape = (height, width - 2 * P + 1, colors)
    output = np.zeros(output_shape)
    
    for c in range(colors):
        output[:, :, c] = calculate_rosenfeld_window(arr[:, :, c], P)

    return output

def calculate_rosenfeld(arr: np.ndarray[np.uint8, np.uint8], P) -> np.ndarray:
    # Assumes one color
    # Rosenfeld operator:
    # gP(n,m) = 1/P * [x(n+P−1,m) + x(n+P−2,m) + … + x(n,m) − x(n−1,m) − x(n−2,m) − … − x(n−P,m)],
    # where P = 1,2,4,8,16,….

    height = arr.shape[0]
    width = arr.shape[1]

    x = arr.T
    g = np.zeros((width, height))

    for n in range(P, width - P + 1):
            sum = np.zeros(height)

            for n_shift in range(-P, P):
                if n_shift >= 0:
                    sum = sum + x[n + n_shift, :]
                else:
                    sum = sum - x[n + n_shift, :]

            g[n, :] = sum / P

    g = g[P : width - P + 1, :].T

    return g

def calculate_rosenfeld_window(arr: np.ndarray, P: int) -> np.ndarray:
    """
    Calculate the Rosenfeld operator using a sliding window approach.

    Parameters:
    arr (np.ndarray): The input image.
    P (int): The size of the window.

    Returns:
    np.ndarray: The output image with the Rosenfeld operator applied.
    """
    
    height = arr.shape[0]
    width = arr.shape[1]

    arr = arr.T

    g = np.zeros((width, height))

    # Calculate the sum of the pixels in the positive direction
    sum_positive = np.cumsum(arr, axis=0)

    # Calculate the sum of the pixels in the negative direction
    sum_negative = np.cumsum(arr[::-1, :], axis=0)

    # Calculate the Rosenfeld operator using the sliding window approach
    for n in range(P, width - P + 1):
            # Calculate the sum of the pixels in the positive direction
            pos_sum = sum_positive[n + P - 1, :] - sum_positive[n - 1, :]
            # Calculate the sum of the pixels in the negative direction
            neg_sum = sum_negative[-n - 1 + P, :] - sum_negative[-n - 1, :]
            # Calculate the Rosenfeld operator
            g[n, :] = (pos_sum - neg_sum) / P

    g = g[P : width - P + 1, :].T

    return g