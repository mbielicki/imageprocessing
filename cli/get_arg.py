from exceptions import ArgumentValueError, MissingArgumentError

def get_arg(args, arg_name):
    try:
        return args[arg_name]
    except KeyError:
        raise MissingArgumentError(f"No {arg_name} given.")

def get_int_arg(args, arg_name):
    try:
        return int(get_arg(args, arg_name))
    except ValueError as e:
        raise ArgumentValueError(f"Incorrect value for {arg_name}: " + e.args[0])

def get_float_arg(args, arg_name):
    try:
        return float(get_arg(args, arg_name))
    except ValueError as e:
        raise ArgumentValueError(f"Incorrect value for {arg_name}: " + e.args[0])