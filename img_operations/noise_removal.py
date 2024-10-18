import numpy as np
from cli.allowed_args import assert_only_allowed_args


def median(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    box_width = 4
    box_height = 4

    def box_values(x, y, c):
        box = []
        for s in range(x - box_width // 2, x + box_width // 2 + 1):
            for t in range(y - box_height // 2, y + box_height // 2 + 1):
                if s >= 0 and s < width and t >= 0 and t < height:
                    box.append(arr[t, s, c])

        return box

    new_arr = np.zeros((height, width, colors))

    for y in range(height):
        for x in range(width):
            for c in range(colors):

                box = box_values(x, y, c)
                new_arr[y, x, c] = np.median(box)

    return new_arr

def gmean():
    pass