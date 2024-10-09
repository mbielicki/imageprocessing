from exceptions import ArgumentError


def args_to_dict(args):
    result = dict()
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=')
            result[key] = value
        else:
            raise ArgumentError("Missing '=' in command line parameter: " + arg)
    return result