import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

from cli.allowed_args import assert_only_allowed_args
from constants import MAX_PIXEL_VALUE
from utils import time_it

from fourier.fft import fft, ifft

@time_it
def fft_img(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr[:, :, 0].astype(np.float32)
    x = x - np.mean(x)

    X = fft2d(x)
    
    img = np.abs(X)
    img = img / np.max(img) * MAX_PIXEL_VALUE

    img = swap_quarters(img)

    fig, ax = plt.subplots()
    N = img.shape[1]
    M = img.shape[0]
    p = ax.pcolor(np.arange(N), np.arange(M), img, vmin=img.min(), vmax=img.max())
    cb = fig.colorbar(p, ax=ax)

    plt.show()


    return img.astype(np.uint8)[:, :, None]

def fft2d(x: np.ndarray) -> np.ndarray:
    N = x.shape[1]
    M = x.shape[0]
    X = np.zeros(shape=(M, N), dtype=np.complex64)

    for m in range(M):
        X[m] = fft(x[m])

    for n in range(N):
        X[:, n] = fft(X[:, n])

    return X

def swap_quarters(img: np.ndarray) -> np.ndarray:
    M, N = img.shape
    new_img = np.zeros(img.shape, dtype=img.dtype)

    top_left = img[:M//2, :N//2]
    top_right = img[:M//2, N//2:]
    bottom_left = img[M//2:, :N//2]
    bottom_right = img[M//2:, N//2:]

    new_img[:M//2, :N//2] = bottom_right
    new_img[:M//2, N//2:] = bottom_left
    new_img[M//2:, :N//2] = top_right
    new_img[M//2:, N//2:] = top_left

    return new_img