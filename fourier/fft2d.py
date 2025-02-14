import numpy as np
import matplotlib.pyplot as plt

from cli.allowed_args import assert_only_allowed_args
from constants import DEBUG_MODE, MAX_PIXEL_VALUE
from fourier.utils import fourier_imgs, swap_quarters
from utils import time_it

from fourier.fft import fft, ifft

@time_it
def fft2d_and_back(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr
    X = fft2d(x)

    X = swap_quarters(X)
    fourier_imgs(X, output_file=args['--output'])
    X = swap_quarters(X)
    
    new_x = ifft2d(X)
    new_x = new_x.real
    new_x = new_x.astype(np.uint8)

    return new_x[:, :, None]

@time_it
def fft_img(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr[:, :, 0].astype(np.float32)
    x = x - np.mean(x)

    X = fft2d(x)
    
    img = np.abs(X)
    img = img / np.max(img) * MAX_PIXEL_VALUE

    img = swap_quarters(img)

    if DEBUG_MODE:
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

def ifft2d(X: np.ndarray) -> np.ndarray:
    N = X.shape[1]
    M = X.shape[0]
    x = np.zeros(shape=(M, N), dtype=np.complex64)

    for m in range(M):
        x[m] = ifft(X[m])

    for n in range(N):
        x[:, n] = ifft(x[:, n])

    return x
