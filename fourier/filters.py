import numpy as np
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_int_arg, get_min_max_args
from fourier.fft2d import fft2d, ifft2d, swap_quarters
from fourier.utils import circle_mask, complex_to_img, fourier_imgs, load_mask
from img_transformations.colors import to_grayscale

def phase_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--l', '--k'])

    x = arr[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape

    dc = X[M//2, N//2]

    l = get_int_arg(args, '--l')
    k = get_int_arg(args, '--k')

    n, m = np.meshgrid(np.arange(N), np.arange(M))
    mask = np.exp(1j * (-n*k*2*np.pi/N -m*l*2*np.pi/M + (k+l)*np.pi))

    X = X * mask

    X[M//2, N//2] = dc

    fourier_imgs(X, output_file=args['--output'])
    
    X = swap_quarters(X)

    new_x = ifft2d(X)

    return complex_to_img(new_x)

def any_filter(args: dict, arr: np.ndarray) -> np.ndarray:
    assert_only_allowed_args(args, ['--input', '--output', '--mask'])

    x = to_grayscale(arr)[:, :, 0]
    X = fft2d(x)

    X = swap_quarters(X)
    M, N = X.shape
    
    dc = X[M//2, N//2]

    mask = load_mask(args['--mask'], (M, N))
    X = X * mask
    
    X[M//2, N//2] = dc

    fourier_imgs(X, output_file=args['--output'])
    
    X = swap_quarters(X)

    new_x = ifft2d(X)

    return complex_to_img(new_x)

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

