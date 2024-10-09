def negative(args, arr, im, numColorChannels):
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            for c in range(numColorChannels):
                new_color = arr[x, y, c] * -1 + 255

                arr[x, y, c] = new_color

def brightness(args, arr, im, numColorChannels):
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            for c in range(numColorChannels):
                strength = int(args['--strength'])

                new_color = arr[x, y, c] + strength
                if new_color > 255:
                    new_color = 255
                elif new_color < 0:
                    new_color = 0

                arr[x, y, c] = new_color

def contrast(args, arr, im, numColorChannels):
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            for c in range(numColorChannels):
                strength = float(args['--strength'])

                if strength < 1:
                    offset = 256/2 
                else:
                    offset = - 256/2
                
                new_color = (arr[x, y, c] * strength) + offset
                if new_color > 255:
                    new_color = 255
                elif new_color < 0:
                    new_color = 0
                    
                arr[x, y, c] = new_color
