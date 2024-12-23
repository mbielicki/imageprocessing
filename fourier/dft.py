import numpy as np
import matplotlib.pyplot as plt
from cli.allowed_args import assert_only_allowed_args
from utils import time_it

@time_it
def dft_and_back(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr.flatten()
    X = dft(x)

    new_x = idft(X).real.astype(np.uint8)

    return new_x.reshape(arr.shape)


def dft(x: np.ndarray) -> np.ndarray:
    N = x.shape[0]
    X = np.zeros(x.shape, dtype=np.complex64)  

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

    return X

def idft(X: np.ndarray) -> np.ndarray:
    N = X.shape[0]
    x = np.zeros(X.shape, dtype=np.complex64)

    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)

    x = x / N

    return x