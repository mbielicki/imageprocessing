def brightness(args, arr, x, y, c):
    strength = int(args['--strength'])

    new_color = arr[x, y, c] + strength
    if new_color > 255:
        new_color = 255
    elif new_color < 0:
        new_color = 0

    arr[x, y, c] = new_color