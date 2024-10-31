import numpy as np

from constants import HISTOGRAM_BG, HISTOGRAM_FG, HISTOGRAM_HEIGHT, PIXEL_VALUE_RANGE
from img_transformations.to_one_channel import to_one_channel


def get_histogram(arr):
    height = arr.shape[0]
    width = arr.shape[1]
    
    hist = np.zeros(PIXEL_VALUE_RANGE, dtype=int)

    for x in range(width):
        for y in range(height):
            value = arr[y, x]
            hist[value] += 1

    return hist

def draw_histogram(args, arr):
    arr = to_one_channel(args, arr)

    hist = get_histogram(arr)
    max_n_pixels = max(hist)

    hist_im = np.empty((HISTOGRAM_HEIGHT, PIXEL_VALUE_RANGE), dtype=np.uint8)
    hist_im.fill(HISTOGRAM_BG)

    for x in range(PIXEL_VALUE_RANGE):
        n_such_pixels = hist[x]
        bar_height = n_such_pixels * HISTOGRAM_HEIGHT // max_n_pixels
        hist_im[:bar_height, x] = HISTOGRAM_FG

    hist_im = hist_im[::-1]

    return hist_im.reshape((HISTOGRAM_HEIGHT, PIXEL_VALUE_RANGE, 1))