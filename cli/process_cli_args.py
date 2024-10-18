import sys

from exceptions import ArgumentError, UnknownArgumentError
from cli.args_to_dict import args_to_dict

from img_operations.elementary import brightness, contrast, negative
from img_operations.geometric import hflip, dflip, resize, vflip
from img_operations.apply_to_image import apply_to_image
from img_operations.noise_removal import gmean_filter, median_filter

from img_comparison.compare_images import compare_images
from img_comparison.similarity import md, mse, pmse, psnr, snr


def process_cli_args():

    if len(sys.argv) == 1:
        raise ArgumentError("No command given.")
    
    command = sys.argv[1]
    args = args_to_dict(sys.argv[2:])
    
    if command == '--help':
        raise NotImplementedError("Help.")
    
    # Elementary operations
    elif command == '--brightness':
        apply_to_image(args, brightness)
    elif command == '--contrast':
        apply_to_image(args, contrast)
    elif command == '--negative':
        apply_to_image(args, negative)

    # Geometric operations
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

    # Noise removal
    elif command == '--median':
        apply_to_image(args, median_filter)
    elif command == '--gmean':
        apply_to_image(args, gmean_filter)

    # Image similarity
    elif command == '--mse':
        message = compare_images(args, mse)
        print(message)
    elif command == '--pmse':
        message = compare_images(args, pmse)
        print(message)
    elif command == '--snr':
        message = compare_images(args, snr)
        print(message)
    elif command == '--psnr':
        message = compare_images(args, psnr)
        print(message)
    elif command == '--md':
        message = compare_images(args, md)
        print(message)
    
    else:
        raise UnknownArgumentError("Unknown command: " + command)
