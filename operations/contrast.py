def contrast(args, arr, x, y, c):
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
