import numpy as np

def circle_mask(shape: tuple, r) -> np.ndarray:

    xn, yn = shape
    
    x_0 = xn//2
    y_0 = yn//2
    x = np.arange(xn)
    y = np.arange(yn)
    x, y = np.meshgrid(x, y)
    mask = np.sqrt((x-x_0)**2+(y-y_0)**2) < r

    return mask