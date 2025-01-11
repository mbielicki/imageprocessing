import numpy as np
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg, get_min_max_args
from fourier.fft2d import fft2d, ifft2d, swap_quarters
from fourier.utils import circle_mask, complex_to_img, fourier_imgs


def band_cut_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--band-min', '--band-max'])
    band_min, band_max = get_min_max_args(args, '--band-min', '--band-max')

    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape
    
    mask = ~circle_mask((M, N), band_max) | circle_mask((M, N), band_min)
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

    mask = circle_mask((M, N), band_max) * ~circle_mask((M, N), band_min)
    X = X * mask

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


    mask = ~circle_mask((M, N), band)
    X = X * mask

    X[M//2, N//2] = dc

    fourier_imgs(X, output_file=args['--output'])

    X = swap_quarters(X)

    new_x = ifft2d(X)
    return complex_to_img(new_x)

