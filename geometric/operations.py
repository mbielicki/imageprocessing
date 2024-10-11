from cli.allowed_args import assert_only_allowed_args


def hflip(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    for y in range(height):
        for x in range(width // 2):
            mirror_x = width - 1 - x
            temp = arr[y, x].copy()
            arr[y, x] = arr[y, mirror_x]
            arr[y, mirror_x] = temp


def vflip(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    for y in range(height // 2):
        for x in range(width):
            mirror_y = height - 1 - y
            temp = arr[y, x].copy()
            arr[y, x] = arr[mirror_y, x]
            arr[mirror_y, x] = temp

def dflip(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    for y in range(height):
        for x in range(width - int(y * width / height)):
            mirror_y = height - 1 - y
            mirror_x = width - 1 - x
            temp = arr[y, x].copy()
            arr[y, x] = arr[mirror_y, mirror_x]
            arr[mirror_y, mirror_x] = temp


def paint(args, arr):
    assert_only_allowed_args(args, [])
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    for x in range(width):
        for y in range(height):
            if y > 100 and y < 200:
                for c in range(colors):
                    arr[y, x, c] = 0
