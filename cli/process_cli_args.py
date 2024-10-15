import sys

from cli.args_to_dict import args_to_dict
from elementary.operations import brightness, contrast, negative
from exceptions import ArgumentError, UnknownArgumentError
from geometric.operations import hflip, dflip, resize, vflip
from apply_to_image import apply_to_image


def process_cli_args():

    if len(sys.argv) == 1:
        raise ArgumentError("No command given.")
    
    command = sys.argv[1]
    args = args_to_dict(sys.argv[2:])
    
    if command == '--brightness':
        apply_to_image(args, brightness)
    elif command == '--contrast':
        apply_to_image(args, contrast)
    elif command == '--negative':
        apply_to_image(args, negative)
    elif command == '--hflip':
        apply_to_image(args, hflip)
    elif command == '--vflip':
        apply_to_image(args, vflip)
    elif command == '--dflip':
        apply_to_image(args, dflip)
    elif command == '--enlarge':
        apply_to_image(args, resize)
    elif command == '--shrink':
        apply_to_image(args, resize)
    elif command == '--test':
        pass #TODO delete
    elif command == '--help':
        raise NotImplementedError("Help.")
    else:
        raise UnknownArgumentError("Unknown command: " + command)
