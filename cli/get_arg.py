from exceptions import ArgumentValueError, MissingArgumentError

def in_range(value: int, range: tuple[int, int]):
    return value >= range[0] and value <= range[1]

def get_min_max_args(args, min_arg_name, max_arg_name, range=None, default=None):
    if range and default:
        if not in_range(default[0], range) or not in_range(default[1], range):
            raise ValueError(f"Default values for {min_arg_name} and {max_arg_name} are out of range.")
    
    min_arg = get_int_arg(args, min_arg_name, range=range, default=default[0])
    max_arg = get_int_arg(args, max_arg_name, range=range, default=default[1])

    if min_arg > max_arg:
        raise ArgumentValueError(f"{min_arg_name} must be less than {max_arg_name}")

    return min_arg, max_arg
    

def get_color_arg(args, arg_name):
    try:
        color = args[arg_name].lower()
    except KeyError:
        raise MissingArgumentError(f"Missing argument: {arg_name}")
    
    
    if color not in ['r', 'g', 'b']:
        raise ArgumentValueError(f"Invalid value for {arg_name}: {color}")
    
    color_vals = {'r': 0, 'g': 1, 'b': 2}
    return color_vals[color]

def get_arg(args, arg_name, default=None):
    try:
        return args[arg_name]
    except KeyError:
        if default is not None:
            return default
        
        raise MissingArgumentError(f"No {arg_name} given.")
    
def get_point_arg(args, arg_name, default=None, range=None):
    arg = get_arg(args, arg_name, default)
    try:
        x, y = arg.split(',')
        x = int(x)
        y = int(y)
    except ValueError as e:
        raise ArgumentValueError(f"Incorrect value for {arg_name}: " + e.args[0])
    
    if range is not None:
        (min_x, min_y), (max_x, max_y) = range
        if not in_range(x, (min_x, max_x)) or not in_range(y, (min_y, max_y)):
            raise ArgumentValueError(f"{arg_name} must be in range {range}")
        
    return x, y


    

def get_int_arg(args, arg_name, range=None, default=None, allowed=None):
    try:
        arg =  int(get_arg(args, arg_name, default))
    except ValueError as e:
        raise ArgumentValueError(f"Incorrect value for {arg_name}: " + e.args[0])
    
    if range is not None:
        min_val, max_val = range
        if arg < min_val:
            raise ArgumentValueError(f"{arg_name} must be >= {min_val}")
        if arg > max_val:
            raise ArgumentValueError(f"{arg_name} must be <= {max_val}")
        
    if allowed is not None:
        if arg not in allowed:
            raise ArgumentValueError(f"{arg_name} must be one of {allowed}")

    return arg

def get_float_arg(args, arg_name):
    try:
        return float(get_arg(args, arg_name))
    except ValueError as e:
        raise ArgumentValueError(f"Incorrect value for {arg_name}: " + e.args[0])

def get_positive_float_arg(args, arg_name):
    try:
        val = float(get_arg(args, arg_name))
        if val <= 0:
            raise ValueError(f"Value must be positive.")
        return float(get_arg(args, arg_name))
    except ValueError as e:
        raise ArgumentValueError(f"Incorrect value for {arg_name}: " + e.args[0])