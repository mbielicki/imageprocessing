import numpy as np
from cli.allowed_args import assert_only_allowed_args
from utils import gmean

def get_box_values(arr, x, y, c, box_width, box_height, img_width, img_height) -> list[int]:
    box = []
    for s in range(x - box_width // 2, x + box_width // 2 + 1):
        for t in range(y - box_height // 2, y + box_height // 2 + 1):
            if s >= 0 and s < img_width and t >= 0 and t < img_height:
                box.append(arr[t, s, c])

    return box

def median_filter(args, arr):
    assert_only_allowed_args(args, ['--input', '--output'])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    BOX_WIDTH = 3
    BOX_HEIGHT = 3

    new_arr = np.zeros((height, width, colors))

    for y in range(height):
        for x in range(width):
            for c in range(colors):

                box = get_box_values(arr, x, y, c, BOX_WIDTH, BOX_HEIGHT, width, height)
                new_arr[y, x, c] = np.median(box)

    return new_arr

def gmean_filter(args, arr):
    assert_only_allowed_args(args, ['--input', '--output'])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    BOX_WIDTH = 3
    BOX_HEIGHT = 3

    new_arr = np.zeros((height, width, colors))

    for y in range(height):
        for x in range(width):
            for c in range(colors):

                box = get_box_values(arr, x, y, c, BOX_WIDTH, BOX_HEIGHT, width, height)
                new_arr[y, x, c] = gmean(box)

    return new_arr