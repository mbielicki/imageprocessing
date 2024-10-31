from typing import Callable
from PIL import Image
import numpy as np

from exceptions import MissingArgumentError
from img_file_to_arr import img_file_to_arr

type ImageTransform = Callable[[dict, np.ndarray], np.ndarray]

def transform_image(args, func: ImageTransform) -> None:
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
    # newIm.show() # uncomment to see the result

    try:
        output_file = args['--output']
    except KeyError:
        output_file = 'output.bmp'

    newIm.save(output_file)
