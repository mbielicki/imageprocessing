from PIL import Image
import numpy as np

def brightness(args):
    input_file = args['--input']
    im = Image.open(input_file)

    arr = np.array(im.getdata()) 
    # arr.shape == (100)
    # arr.shape == (100, 3)
    
    if arr.ndim == 1: #grayscale
        numColorChannels = 1
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
        # arr.shape == (10, 10, 1)
    else:
        numColorChannels = arr.shape[1]
        arr = arr.reshape(im.size[1], im.size[0], numColorChannels)
        # arr.shape == (10, 10, 3)

    strength = int(args['--strength'])

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            for c in range(numColorChannels):
                new_color = arr[x, y, c] + strength
                if new_color > 255:
                    new_color = 255
                elif new_color < 0:
                    new_color = 0
                arr[x, y, c] = new_color

    newIm = Image.fromarray(arr.astype(np.uint8))
    newIm.show()
    newIm.save(args['--output'])
