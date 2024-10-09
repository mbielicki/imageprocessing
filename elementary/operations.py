def negative(args, arr):
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    for x in range(width):
        for y in range(height):
            for c in range(colors):

                new_color = arr[x, y, c] * -1 + 255
                arr[x, y, c] = new_color

def brightness(args, arr):
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    
    strength = int(args['--strength'])

    for x in range(width):
        for y in range(height):
            for c in range(colors):
                
                new_color = arr[x, y, c] + strength
                if new_color > 255:
                    new_color = 255
                elif new_color < 0:
                    new_color = 0

                arr[x, y, c] = new_color

def contrast(args, arr):
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    strength = float(args['--strength'])
    offset = 256/2 * (1 if strength < 1 else -1)
    
    for x in range(width):
        for y in range(height):
            for c in range(colors):
                
                new_color = (arr[x, y, c] * strength) + offset
                if new_color > 255:
                    new_color = 255
                elif new_color < 0:
                    new_color = 0
                    
                arr[x, y, c] = new_color
