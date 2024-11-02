import numpy as np
from cli.allowed_args import assert_only_allowed_args
from constants import PIXEL_VALUE_RANGE
from histogram import get_histogram
from img_transformations.colors import to_grayscale

def calculate_mean(arr: np.ndarray) -> float:
    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height
    L = PIXEL_VALUE_RANGE
    
    hist = get_histogram(arr)

    return np.multiply(hist, np.arange(L), out=hist).sum() / N


def cmean(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(args, arr)

    mean = calculate_mean(arr)

    return f"Mean: {mean:.2f}"

def calculate_variance(arr: np.ndarray) -> float:
    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height
    L = PIXEL_VALUE_RANGE
    
    hist = get_histogram(arr)

    mean = calculate_mean(arr)

    return np.multiply(hist, np.power(np.arange(L) - mean, 2)).sum() / N

def cvariance(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(args, arr)

    variance = calculate_variance(arr)

    return f"Variance: {variance:.2f}"

def calculate_stdev(arr: np.ndarray) -> float:
    return np.sqrt(calculate_variance(arr))

def cstdev(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(args, arr)

    stdev = calculate_stdev(arr)

    return f"Standard deviation: {stdev:.2f}"

def cvarcoi(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(args, arr)

    varcoi = calculate_stdev(arr) / calculate_mean(arr)

    return f"Variation Coefficient: {varcoi:.2f}"

def casyco(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(args, arr)

    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height
    L = PIXEL_VALUE_RANGE
    
    hist = get_histogram(arr)

    mean = calculate_mean(arr)
    stdev = calculate_stdev(arr)

    asyco = np.multiply(hist, np.power(np.arange(L) - mean, 3)).sum() / N / np.power(stdev, 3)

    return f"Asymmetry Coefficient: {asyco:.2f}"

def cflatco(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(args, arr)

    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height  
    L = PIXEL_VALUE_RANGE
    
    hist = get_histogram(arr)
    mean = calculate_mean(arr)
    stdev = calculate_stdev(arr)
    m = np.arange(L)

    flatco = ((m - mean) ** 4 * hist - 3).sum() / N / stdev ** 4

    return f"Flatness Coefficient: {flatco:.2f}"