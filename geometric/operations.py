import numpy as np
from cli.allowed_args import assert_only_allowed_args
from cli.get_arg import get_float_arg, get_positive_float_arg
from geometric.interpolation import bilinear_interpolate


def hflip(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    for y in range(height):
        for x in range(width // 2):
            mirror_x = width - 1 - x
            temp = arr[y, x].copy()
            arr[y, x] = arr[y, mirror_x]
            arr[y, mirror_x] = temp
            
    return arr


def vflip(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    for y in range(height // 2):
        for x in range(width):
            mirror_y = height - 1 - y
            temp = arr[y, x].copy()
            arr[y, x] = arr[mirror_y, x]
            arr[mirror_y, x] = temp

    return arr

def dflip(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    for y in range(height):
        for x in range(width - int(y * width / height)):
            mirror_y = height - 1 - y
            mirror_x = width - 1 - x
            temp = arr[y, x].copy()
            arr[y, x] = arr[mirror_y, mirror_x]
            arr[mirror_y, mirror_x] = temp

    return arr

def resize(args, arr):
    assert_only_allowed_args(args, ['--proportion'])
    
    proportion = get_positive_float_arg(args, '--proportion')
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    new_height = int(height * proportion)
    new_width = int(width * proportion)

    new_arr = np.zeros((new_height, new_width, colors))

    for y in range(new_height):
        for x in range(new_width):
            x_as_old_size = x / (new_width - 1) * (width - 1)
            y_as_old_size = y / (new_height - 1) * (height - 1)
            new_arr[y, x] = bilinear_interpolate(arr, x_as_old_size, y_as_old_size)

    return new_arr

