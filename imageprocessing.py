import sys
from exceptions import ApplicationError, ArgumentError, UnknownArgumentError
from process_image import process_image
from elementary.operations import negative, brightness, contrast
from geometric.operations import paint, hflip


def args_to_dict(args):
    result = dict()
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=')
            result[key] = value
        else:
            raise ArgumentError("Missing '=' in command line parameter: " + arg)
    return result


def process_cli_args():

    if len(sys.argv) == 1:
        raise ArgumentError("No command given.")
    
    command = sys.argv[1]
    args = args_to_dict(sys.argv[2:])
    
    if command == '--brightness':
        process_image(args, brightness)
    elif command == '--contrast':
        process_image(args, contrast)
    elif command == '--negative':
        process_image(args, negative)
    elif command == '--hflip':
        process_image(args, hflip)
    elif command == '--test':
        process_image(args, paint)
    else:
        raise UnknownArgumentError("Unknown command: " + command)


def main():
    try:
        process_cli_args()
    except ApplicationError as e:
        print(e)


if __name__ == "__main__":
    main()