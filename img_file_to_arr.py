from PIL import Image
import numpy as np

from exceptions import InputFileError

def img_file_to_arr(file_name: str) -> np.ndarray:
    try:
        im = Image.open(file_name)
    except FileNotFoundError:
        raise InputFileError("File not found: " + file_name)
    except PermissionError as e:
        raise InputFileError("Permission denied: " + e.filename)

    arr = np.array(im.getdata()) 
    
    if arr.ndim == 1: #grayscale
        numColorChannels = 1
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
    else:
        numColorChannels = arr.shape[1]
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)

    return arr