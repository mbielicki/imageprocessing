import numpy as np
import matplotlib.pyplot as plt
from cli.allowed_args import assert_only_allowed_args
from utils import time_it

def dft_and_back(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr.flatten()
    X = dft(x)

    new_x = idft(X).real.astype(np.uint8)

    return new_x.reshape(arr.shape)


@time_it
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


@time_it
def fft_and_back(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output'])

    x = arr.flatten().astype(np.complex64)
    X = fft(x, x.shape[0], 1)

    plt.plot(np.abs(X))
    plt.xscale('log')
    # plt.show()

    return arr
    # new_x = idft(X).real.astype(np.uint8)

    # return new_x.reshape(arr.shape)

last: str = ''
def log(k: int, indentation: int):
    global last
    kstr = str(k)
    if k < 10: kstr = ' ' + kstr
    new = last[0:indentation*3] + ' ' + kstr
    last = new
    print(new)

def fft(x: np.ndarray,  N: int, s: int = 1) -> np.ndarray:
    X = np.zeros(shape=N, dtype=np.complex64)  

    if N == 1:
        X[0] = x[0]
        return X
    
    indentation = int(6 - np.log2(N))

    X[:N//2] = fft(x, N//2, 2*s)
    X[N//2:] = fft(x+s, N//2, 2*s)

    for k in range(N // 2):
        if N > 2: log(k, indentation)

        p = X[k]
        q = np.exp(2j * np.pi * k / N) * X[k + N//2]

        X[k] = p + q
        X[k + N//2] = p - q    

    return X