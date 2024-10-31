import numpy as np
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_min_max_args
from constants import MAX_PIXEL_VALUE
from histogram import get_histogram


def hpower(args, arr):
    assert_only_allowed_args(args, ['--gmin', '--gmax', '--input', '--output'])
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    gmin, gmax = get_min_max_args(args, '--gmin', '--gmax', range=(0, MAX_PIXEL_VALUE), default=(0, MAX_PIXEL_VALUE))


    c1 = gmin ** (1/3)
    c2 = gmax ** (1/3)
    c3 = c2 - c1

    N = width * height
    hist = get_histogram(arr)
    f = arr

    def hist_sum(f: int):
        return hist[:f].sum()
    
    hist_sum = np.frompyfunc(hist_sum, 1, 1)

    g = (c1 + c3 * hist_sum(f) / N) ** 3

    return g
