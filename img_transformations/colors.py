import numpy as np
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_color_arg


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
        