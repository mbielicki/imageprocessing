import math
import numpy as np

def bilinear_interpolate(arr : np.array, x: int, y: int) -> float:
    """
    Interpolate the value of arr at x and y, which is between 0 and width and height of arr.

    :param arr: The array to interpolate.
    :param x: The position in the array to interpolate in the x direction.
    :param y: The position in the array to interpolate in the y direction.
    :return: The interpolated value of arr at x and y.
    """
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    if x >= width - 1:
        x = width - 1

    if y >= height - 1:
        y = height - 1

    if x < 0:
        x = 0

    if y < 0:
        y = 0

    x_0 = math.floor(x)
    x_1 = math.floor(x + 1)
    y_0 = math.floor(y)
    y_1 = math.floor(y + 1)

    f_xy = np.zeros(colors)
    for c in range(colors):

        f_00 = arr[y_0, x_0, c]

        if x >= width - 1:
            f_10 = arr[y_0, x_0, c]
        else:
            f_10 = arr[y_0, x_1, c]

        if y >= height - 1:
            f_01 = arr[y_0, x_0, c]
        else:
            f_01 = arr[y_1, x_0, c]

        if x >= width - 1 and not y >= height - 1:
            f_11 = arr[y_1, x_0, c]
        elif not x >= width - 1 and y >= height - 1:
            f_11 = arr[y_0, x_1, c]
        elif x >= width - 1 and y >= height - 1:
            f_11 = arr[y_0, x_0, c]
        else:
            f_11 = arr[y_1, x_1, c]

        a1 = (x_1 - x) / (x_1 - x_0)
        a2 = (x - x_0) / (x_1 - x_0)

        f_x0 = a1 * f_00 + a2 * f_10
        f_x1 = a1 * f_01 + a2 * f_11

        b1 = (y_1 - y) / (y_1 - y_0)
        b2 = (y - y_0) / (y_1 - y_0)

        f_xy[c] = b1 * f_x0 + b2 * f_x1
    
    return f_xy