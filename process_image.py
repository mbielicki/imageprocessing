import sys
from PIL import Image
import numpy as np

def process_image(args, func):
    try:
        input_file = args['--input']
        im = Image.open(input_file)
    except KeyError:
        print("No input file given.")
        sys.exit()
    except FileNotFoundError:
        print("File not found: " + input_file)
        sys.exit()

    arr = np.array(im.getdata()) 
    
    if arr.ndim == 1: #grayscale
        numColorChannels = 1
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
    else:
        numColorChannels = arr.shape[1]
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)

    func(args, arr)

    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.show() #TODO: remove

    try:
        output_file = args['--output']
    except KeyError:
        output_file = 'output.bmp'
        
    newIm.save(output_file)
