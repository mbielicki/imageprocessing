from PIL import Image
import numpy as np

def process_image(args, func):
    input_file = args['--input']
    im = Image.open(input_file)

    arr = np.array(im.getdata()) 
    
    if arr.ndim == 1: #grayscale
        numColorChannels = 1
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
    else:
        numColorChannels = arr.shape[1]
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)


    for x in range(im.size[0]):
        for y in range(im.size[1]):
            for c in range(numColorChannels):
                func(args, arr, x, y, c)

    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.show()
    newIm.save(args['--output'])