import numpy as np
from constants import PIXEL_VALUE_RANGE
from histogram import get_histogram


def mean(args: dict, arr: np.ndarray) -> str:
    width = arr.shape[1]
    height = arr.shape[0]
    colors = arr.shape[2]

    N = width * height
    L = PIXEL_VALUE_RANGE
    
    hist = get_histogram(arr)

    mean = np.multiply(hist, np.arange(L), out=hist).sum() / N

    return f"Mean: {mean:.2f}"