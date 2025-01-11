import numpy as np
from PIL import Image

from constants import MAX_PIXEL_VALUE
from img_file_to_arr import img_file_to_arr
from img_transformations.colors import as_binary

def load_mask(file_path: str, shape: tuple) -> np.ndarray:
    mask = img_file_to_arr(file_path)
    mask = as_binary(mask)
    mask = resize(mask, shape)
    return mask

def resize(arr: np.ndarray, new_size: tuple) -> np.ndarray:
    if arr.shape == new_size:
        return arr
    
    height, width = arr.shape
    new_height, new_width = new_size

    new_arr = np.zeros((new_height, new_width), dtype=arr.dtype)

    for y in range(new_height):
        for x in range(new_width):
            x_as_old_size = x / (new_width - 1) * (width - 1)
            x_as_old_size = round(x_as_old_size)
            y_as_old_size = y / (new_height - 1) * (height - 1)
            y_as_old_size = round(y_as_old_size)

            new_arr[y, x] = arr[y_as_old_size, x_as_old_size]

    return new_arr

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


def fourier_imgs(X: np.ndarray, output_file: str) -> None:
    mags = np.abs(X)
    mags = np.log10(mags, where=mags>0)
    mags[mags<0] = 0
    mags = mags / np.max(mags) * MAX_PIXEL_VALUE

    Image.fromarray(mags.astype(np.uint8)).save(output_file[:-4] + '-magnitude.bmp')

    phases = np.angle(X)
    phases = (phases + np.pi) / (2 * np.pi) * MAX_PIXEL_VALUE
    Image.fromarray(phases.astype(np.uint8)).save(output_file[:-4] + '-phase.bmp')