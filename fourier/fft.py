import numpy as np
import matplotlib.pyplot as plt
from cli.allowed_args import assert_only_allowed_args

def fft_and_back(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr.flatten()
    X = fft(x)

    new_x = ifft(X)
    new_x = new_x.real
    new_x = new_x.astype(np.uint8)

    return new_x.reshape(arr.shape)

def fft(x: np.ndarray) -> np.ndarray:
    N = x.shape[0]

    if N == 1:
        return np.array([x[0]], dtype=np.complex64)

    E = fft(x[0:N:2]) # even
    O = fft(x[1:N:2]) # odd

    X = np.zeros(shape=N, dtype=np.complex64)  

    for k in range(N // 2):
        p = E[k]
        q = np.exp(-2j * np.pi * k / N) * O[k]

        X[k] = p + q
        X[k + N//2] = p - q    

    return X

def ifft(X: np.ndarray) -> np.ndarray:
    N = X.shape[0]
    return ifft_sum(X) / N

def ifft_sum(X: np.ndarray) -> np.ndarray:
    N = X.shape[0]

    if N == 1:
        return np.array([X[0]], dtype=np.complex64)

    E = ifft_sum(X[0:N:2]) # even
    O = ifft_sum(X[1:N:2]) # odd

    x = np.zeros(shape=N, dtype=np.complex64)  

    for k in range(N // 2):
        p = E[k]
        q = np.exp(2j * np.pi * k / N) * O[k]

        x[k] = (p + q)
        x[k + N//2] = (p - q)

    return x