import numpy as np


def complex_to_img(x: np.ndarray) -> np.ndarray:
    new_x = x.real
    new_x = np.where(new_x < 0, 0, new_x)
    new_x = np.where(new_x > MAX_PIXEL_VALUE, MAX_PIXEL_VALUE, new_x)
    new_x = new_x.astype(np.uint8)

    return new_x[:, :, None]

def circle_mask(shape: tuple, r) -> np.ndarray:

    xn, yn = shape
    
    x_0 = xn//2
    y_0 = yn//2
    x = np.arange(xn)
    y = np.arange(yn)
    x, y = np.meshgrid(x, y)
    mask = np.sqrt((x-x_0)**2+(y-y_0)**2) < r

    return mask