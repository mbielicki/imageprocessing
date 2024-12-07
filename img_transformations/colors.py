import numpy as np
from cli.get_arg import get_color_arg
from constants import MAX_PIXEL_VALUE


def extract_one_channel(args, arr):

    colors = arr.shape[2]

    if colors > 1:
        channel = get_color_arg(args, '--channel')
    else:
        channel = 0

    return arr[:, :, channel]

def to_grayscale(args, arr):
    width = arr.shape[1]
    height = arr.shape[0]
    colors = arr.shape[2]

    if colors == 1:
        return arr

    gray_arr = np.zeros((height, width, 1), dtype=np.uint8)

    for x in range(width):
        for y in range(height):
            gray_arr[y, x] = arr[y, x, 0] * 0.299 + arr[y, x, 1] * 0.587 + arr[y, x, 2] * 0.114

    return gray_arr
        

def as_binary(arr: np.ndarray) -> np.ndarray:
    return (arr > 0)[:, :, 0]

def as_bw(arr: np.ndarray) -> np.ndarray:
    return np.where(arr > 0, MAX_PIXEL_VALUE, 0)[:, :, None]

def bw_to_indices(arr: np.ndarray) -> np.ndarray:
    return np.transpose(np.nonzero(arr == 1))

def remove_outside_indices(indices: np.ndarray, shape: tuple):
    """
    Remove 2D indices that are out of bounds for the given shape.
    
    Parameters:
    -----------
    indices : set or array-like
        A set of (row, col) indices to filter
    shape : tuple
        The shape of the 2D array (rows, columns)
    
    Returns:
    --------
    set
        A set of indices within the bounds of the given shape
    """
    # Create masks for row and column bounds
    row_mask = (indices[:, 0] >= 0) & (indices[:, 0] < shape[0])
    col_mask = (indices[:, 1] >= 0) & (indices[:, 1] < shape[1])
    
    # Combine masks and filter indices
    valid_indices_mask = row_mask & col_mask
    valid_indices = indices[valid_indices_mask]
    
    # Convert back to set
    return valid_indices

def indices_to_bw(set: np.ndarray, shape: tuple, offset: tuple = (0, 0)) -> np.ndarray:
    set += offset

    set = remove_outside_indices(set, shape)
    indices = tuple(set.T)

    arr = np.zeros(shape, dtype=np.bool)
    arr[indices] = 1

    return arr