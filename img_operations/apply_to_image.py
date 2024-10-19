from typing import Callable
from PIL import Image
import numpy as np

from exceptions import MissingArgumentError
from img_file_to_arr import img_file_to_arr

def apply_to_image(args, func: Callable[[dict, np.ndarray], np.ndarray]) -> None:
    try:
        input_file = args['--input']
    except KeyError:
        raise MissingArgumentError("No input file given.")
    
    arr = img_file_to_arr(input_file)

    arr = func(args, arr)
    arr = arr.astype(np.uint8)

    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    if colors == 1:
        arr = arr.reshape((height, width))

    newIm = Image.fromarray(arr)
    newIm.show() #TODO: remove

    try:
        output_file = args['--output']
    except KeyError:
        output_file = 'output.bmp'

    newIm.save(output_file)
