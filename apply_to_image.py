from PIL import Image
import numpy as np

from exceptions import InputFileError, MissingArgumentError

def apply_to_image(args, func):
    try:
        input_file = args['--input']
    except KeyError:
        raise MissingArgumentError("No input file given.")
    
    try:
        im = Image.open(input_file)
    except FileNotFoundError:
        raise InputFileError("File not found: " + input_file)
    except PermissionError as e:
        raise InputFileError("Permission denied: " + e.filename)

    arr = np.array(im.getdata()) 
    
    if arr.ndim == 1: #grayscale
        numColorChannels = 1
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
    else:
        numColorChannels = arr.shape[1]
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)

    arr = func(args, arr)

    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.show() #TODO: remove

    try:
        output_file = args['--output']
    except KeyError:
        output_file = 'output.bmp'

    newIm.save(output_file)
