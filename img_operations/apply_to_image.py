from PIL import Image
import numpy as np

from exceptions import MissingArgumentError
from img_file_to_arr import img_file_to_arr

def apply_to_image(args, func):
    try:
        input_file = args['--input']
    except KeyError:
        raise MissingArgumentError("No input file given.")
    
    arr = img_file_to_arr(input_file)

    arr = func(args, arr)

    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.show() #TODO: remove

    try:
        output_file = args['--output']
    except KeyError:
        output_file = 'output.bmp'

    newIm.save(output_file)
