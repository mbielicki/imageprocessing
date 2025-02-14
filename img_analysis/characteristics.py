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
    arr = to_grayscale(arr)

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
    arr = to_grayscale(arr)

    variance = calculate_variance(arr)

    return f"Variance: {variance:.2f}"

def calculate_stdev(arr: np.ndarray) -> float:
    return np.sqrt(calculate_variance(arr))

def cstdev(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(arr)

    stdev = calculate_stdev(arr)

    return f"Standard deviation: {stdev:.2f}"

def cvarcoi(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(arr)

    varcoi = calculate_stdev(arr) / calculate_mean(arr)

    return f"Variation Coefficient I: {varcoi:.2f}"

def casyco(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(arr)

    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height
    L = PIXEL_VALUE_RANGE
    
    hist = get_histogram(arr)

    mean = calculate_mean(arr)
    stdev = calculate_stdev(arr)
    m = np.arange(L)

    asyco = ((m - mean) ** 3 * hist).sum() / N / stdev ** 3

    return f"Asymmetry Coefficient: {asyco:.2f}"

def cflatco(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(arr)

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

def cvarcoii(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(arr)

    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height  
    
    hist = get_histogram(arr)

    varcoii = (hist ** 2).sum() / N / N

    return f"Variation Coefficient II: {varcoii:.2f}"

def centropy(args: dict, arr: np.ndarray) -> str:
    assert_only_allowed_args(args, ['--input'])
    arr = to_grayscale(arr)
    
    width = arr.shape[1]
    height = arr.shape[0]

    N = width * height  
    
    hist = get_histogram(arr)
    hist_no_zeros = hist[hist > 0]

    entropy = - (hist_no_zeros * np.log2(hist_no_zeros / N)).sum() / N

    return f"Information source entropy: {entropy:.2f}"