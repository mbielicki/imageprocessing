import numpy as np
from PIL import Image
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg, get_min_max_args
from constants import MAX_PIXEL_VALUE
from fourier.fft2d import fft2d, ifft2d, swap_quarters
from fourier.utils import circle_mask, complex_to_img


def band_cut_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--band-min', '--band-max'])
    band_min, band_max = get_min_max_args(args, '--band-min', '--band-max')

    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape
    
    mask = np.ones(shape=(M, N), dtype=bool)

    mask[M//2-band_max:M//2+band_max, N//2-band_max:N//2+band_max] = False
    mask[M//2-band_min:M//2+band_min, N//2-band_min:N//2+band_min] = True

    X = X * mask

    fourier_imgs(X, output_file=args['--output'])
    
    X = swap_quarters(X)

    new_x = ifft2d(X)

    return complex_to_img(new_x)

def band_pass_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--band-min', '--band-max'])
    band_min, band_max = get_min_max_args(args, '--band-min', '--band-max')

    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape
    
    dc = X[M//2, N//2]

    X[:M//2-band_max] = 0
    X[M//2+band_max:] = 0
    X[:, :N//2-band_max] = 0
    X[:, N//2+band_max:] = 0
    
    X[M//2-band_min:M//2+band_min, N//2-band_min:N//2+band_min] = 0

    X[M//2, N//2] = dc

    fourier_imgs(X, output_file=args['--output'])
    
    X = swap_quarters(X)

    new_x = ifft2d(X)

    return complex_to_img(new_x)


def low_pass_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--band'])

    band = get_int_arg(args, '--band')

    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape

    mask = circle_mask((M, N), band)
    X = X * mask

    fourier_imgs(X, output_file=args['--output'])

    X = swap_quarters(X)

    new_x = ifft2d(X)
    return complex_to_img(new_x)


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
    return complex_to_img(new_x)


def fourier_imgs(X: np.ndarray, output_file: str) -> None:
    mags = np.abs(X)
    mags = np.log10(mags, where=mags>0)
    mags[mags<0] = 0
    mags = mags / np.max(mags) * MAX_PIXEL_VALUE

    Image.fromarray(mags.astype(np.uint8)).save(output_file[:-4] + '-magnitude.bmp')

    phases = np.angle(X)
    phases = (phases + np.pi) / (2 * np.pi) * MAX_PIXEL_VALUE
    Image.fromarray(phases.astype(np.uint8)).save(output_file[:-4] + '-phase.bmp')