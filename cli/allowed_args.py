from exceptions import ArgumentError


def assert_only_allowed_args(args: dict, allowed_args: list):
    allowed_args += ['--input', '--output']
    
    for arg in args.keys():
        if arg not in allowed_args:
            raise ArgumentError("Unknown command line parameter: " + arg)
        