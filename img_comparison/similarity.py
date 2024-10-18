import numpy as np


def mse(args: dict, input_im: np.ndarray, ref_im: np.ndarray) -> str:

    width = input_im.shape[1]
    height = input_im.shape[0]
    colors = input_im.shape[2]

    for x in range(width):
        for y in range(height):
            for c in range(colors):
                input_im[y, x, c] -= ref_im[y, x, c]

    mse = np.mean(np.square(input_im))

    return f"Mean Square Error: {mse}"