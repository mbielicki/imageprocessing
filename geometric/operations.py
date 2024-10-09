def hflip(args, arr, im, numColorChannels):
    width = arr.shape[1]
    height = arr.shape[0]
    for y in range(height):
        for x in range(width // 2):
            mirror_x = width - 1 - x
            temp = arr[y, x].copy()
            arr[y, x] = arr[y, mirror_x]
            arr[y, mirror_x] = temp

def paint(args, arr, im, numColorChannels):
    width = arr.shape[1]
    height = arr.shape[0]

    for x in range(width):
        for y in range(height):
            if y > 100 and y < 200:
                for c in range(numColorChannels):
                    arr[y, x, c] = 0
