from cli.get_arg import get_float_arg, get_int_arg
from constants import MAX_PIXEL_VALUE, PIXEL_VALUE_RANGE
from exceptions import ArgumentValueError, MissingArgumentError
from cli.allowed_args import assert_only_allowed_args


def negative(args, arr):
    assert_only_allowed_args(args, ['--input', '--output'])

    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    for x in range(width):
        for y in range(height):
            for c in range(colors):

                new_color = arr[x, y, c] * -1 + MAX_PIXEL_VALUE
                arr[x, y, c] = new_color
                
    return arr

def brightness(args, arr):
    assert_only_allowed_args(args, ['--strength', '--input', '--output'])

    strength = get_int_arg(args, '--strength')

    try:
        strength = int(args['--strength'])
    except KeyError:
        raise MissingArgumentError("No strength given.")
    except ValueError as e:
        raise ArgumentValueError("Incorrect value for strength: " + e.args[0])
    

    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]

    for x in range(width):
        for y in range(height):
            for c in range(colors):
                
                new_color = arr[x, y, c] + strength
                if new_color > MAX_PIXEL_VALUE:
                    new_color = MAX_PIXEL_VALUE
                elif new_color < 0:
                    new_color = 0

                arr[x, y, c] = new_color
                
    return arr

def contrast(args, arr):
    assert_only_allowed_args(args, ['--strength', '--input', '--output'])

    strength = get_float_arg(args, '--strength')
    
    height = arr.shape[0]
    width = arr.shape[1]
    colors = arr.shape[2]
    
    offset = PIXEL_VALUE_RANGE/2 * (1 if strength < 1 else -1)
    
    for x in range(width):
        for y in range(height):
            for c in range(colors):
                
                new_color = (arr[x, y, c] * strength) + offset
                if new_color > MAX_PIXEL_VALUE:
                    new_color = MAX_PIXEL_VALUE
                elif new_color < 0:
                    new_color = 0
                    
                arr[x, y, c] = new_color
                
    return arr
