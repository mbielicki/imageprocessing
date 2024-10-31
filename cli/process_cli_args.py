import sys

from exceptions import ArgumentError, UnknownArgumentError
from cli.args_to_dict import args_to_dict
from cli.help_message import help_message

from histogram import draw_histogram
from img_transformations.elementary import brightness, contrast, negative
from img_transformations.geometric import hflip, dflip, resize, vflip
from img_transformations.hpower import hpower
from img_transformations.transform_image import transform_image
from img_transformations.noise_removal import gmean_filter, median_filter

from img_comparison.compare_images import compare_images
from img_comparison.similarity import md, mse, pmse, psnr, snr


def process_cli_args():

    if len(sys.argv) == 1:
        raise ArgumentError("No command given.")
    
    command = sys.argv[1]
    args = args_to_dict(sys.argv[2:])
    
    if command == '--help':
        print(help_message)
    
    # Elementary operations
    elif command == '--brightness':
        transform_image(args, brightness)
    elif command == '--contrast':
        transform_image(args, contrast)
    elif command == '--negative':
        transform_image(args, negative)

    # Geometric operations
    elif command == '--hflip':
        transform_image(args, hflip)
    elif command == '--vflip':
        transform_image(args, vflip)
    elif command == '--dflip':
        transform_image(args, dflip)
    elif command == '--enlarge':
        transform_image(args, resize)
    elif command == '--shrink':
        transform_image(args, resize)

    # Noise removal
    elif command == '--median':
        transform_image(args, median_filter)
    elif command == '--gmean':
        transform_image(args, gmean_filter)

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

    # Task 2
    elif command == '--histogram':
        transform_image(args, draw_histogram)
    elif command == '--hpower':
        transform_image(args, hpower)
    
    else:
        raise UnknownArgumentError("Unknown command: " + command)
