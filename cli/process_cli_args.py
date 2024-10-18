import sys

from exceptions import ArgumentError, UnknownArgumentError
from cli.args_to_dict import args_to_dict

from img_operations.elementary import brightness, contrast, negative
from img_operations.geometric import hflip, dflip, resize, vflip
from img_operations.apply_to_image import apply_to_image
from img_operations.noise_removal import gmean_filter, median_filter

from img_comparison.compare_images import compare_images
from img_comparison.similarity import mse


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
    elif command == '--median':
        apply_to_image(args, median_filter)
    elif command == '--gmean':
        apply_to_image(args, gmean_filter)
    elif command == '--mse':
        message = compare_images(args, mse)
        print(message)
    elif command == '--test':
        pass #TODO delete
    elif command == '--help':
        raise NotImplementedError("Help.")
    else:
        raise UnknownArgumentError("Unknown command: " + command)
