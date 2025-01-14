import numpy as np

from cli.allowed_args import assert_only_allowed_args
from fourier.utils import swap_quarters
from fourier.utils import fourier_imgs
from utils import time_it

from fourier.dft import dft, idft


@time_it
def dft2d_and_back(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr[:, :, 0]
    X = dft2d(x)
    
    X = swap_quarters(X)
    fourier_imgs(X, output_file=args['--output'])
    X = swap_quarters(X)

    new_x = idft2d(X)
    new_x = new_x.real
    new_x = new_x.astype(np.uint8)

    return new_x[:, :, None]

def dft2d(x: np.ndarray) -> np.ndarray:
    N = x.shape[1]
    M = x.shape[0]
    X = np.zeros(shape=(M, N), dtype=np.complex64)

    for m in range(M):
        X[m] = dft(x[m])

    for n in range(N):
        X[:, n] = dft(X[:, n])

    return X

def idft2d(X: np.ndarray) -> np.ndarray:
    N = X.shape[1]
    M = X.shape[0]
    x = np.zeros(shape=(M, N), dtype=np.complex64)

    for m in range(M):
        x[m] = idft(X[m])

    for n in range(N):
        x[:, n] = idft(x[:, n])

    return x