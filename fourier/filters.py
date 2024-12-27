import numpy as np
from PIL import Image
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg
from constants import MAX_PIXEL_VALUE
from fourier.fft2d import fft2d, ifft2d, swap_quarters


def low_pass_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--band'])

    band = get_int_arg(args, '--band')


    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape
    X[:M//2-band] = 0
    X[M//2+band:] = 0
    X[:, :N//2-band] = 0
    X[:, N//2+band:] = 0

    fourier_imgs(X, output_file=args['--output'])

    X = swap_quarters(X)

    new_x = ifft2d(X)
    new_x = new_x.real
    new_x = new_x.astype(np.uint8)

    return new_x[:, :, None]


def high_pass_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--band'])

    band = get_int_arg(args, '--band')

    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape
    dc = X[M//2, N//2]

    X[M//2-band:M//2+band, N//2-band:N//2+band] = 0

    X[M//2, N//2] = dc

    fourier_imgs(X, output_file=args['--output'])

    X = swap_quarters(X)

    new_x = ifft2d(X)
    new_x = new_x.real
    new_x = new_x.astype(np.uint8)

    return new_x[:, :, None]


def fourier_imgs(X: np.ndarray, output_file: str) -> None:
    mags = np.abs(X)
    mags = np.log10(mags, where=mags>0)
    mags[mags<0] = 0
    mags = mags / np.max(mags) * MAX_PIXEL_VALUE

    Image.fromarray(mags.astype(np.uint8)).save(output_file[:-4] + '-magnitude.bmp')

    phases = np.angle(X)
    phases = (phases + np.pi) / (2 * np.pi) * MAX_PIXEL_VALUE
    Image.fromarray(phases.astype(np.uint8)).save(output_file[:-4] + '-phase.bmp')