import sys

from cli.args_to_dict import args_to_dict
from elementary.operations import brightness, contrast, negative
from exceptions import ArgumentError, UnknownArgumentError
from geometric.operations import hflip, dflip, vflip
from process_image import process_image


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
    elif command == '--vflip':
        process_image(args, vflip)
    elif command == '--dflip':
        process_image(args, dflip)
    else:
        raise UnknownArgumentError("Unknown command: " + command)
