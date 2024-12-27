import sys

from fourier.dft2d import dft2d_and_back
from fourier.fft2d import fft_img, fft2d_and_back
from exceptions import ArgumentError, UnknownArgumentError
from cli.args_to_dict import args_to_dict
from cli.help_message import help_message

from fourier.filters import band_pass_filter, high_pass_filter, low_pass_filter
from histogram import draw_histogram
from img_analysis.characteristics import casyco, centropy, cflatco, cmean, cstdev, cvarcoi, cvarcoii, cvariance
from img_transformations.convolution import edge_sharpening, orosenfeld
from img_transformations.elementary import brightness, contrast, negative
from img_transformations.geometric import hflip, dflip, resize, vflip
from img_transformations.hpower import hpower
from img_transformations.morphological import closing, dilation, erosion, hmt, m3, opening
from img_transformations.region_growing import region_growing
from img_transformations.transform_image import transform_image
from img_transformations.noise_removal import gmean_filter, median_filter

from img_analysis.analyze_images import compare_images, analyze_images
from img_analysis.similarity import md, mse, pmse, psnr, snr


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
    # Histogram
    elif command == '--histogram':
        transform_image(args, draw_histogram)
    elif command == '--hpower':
        transform_image(args, hpower)

    # Characteristics
    elif command == '--cmean':
        message = analyze_images(args, cmean)
        print(message)
    elif command == '--cvariance':
        message = analyze_images(args, cvariance)
        print(message)
    elif command == '--cstdev':
        message = analyze_images(args, cstdev)
        print(message)
    elif command == '--cvarcoi':
        message = analyze_images(args, cvarcoi)
        print(message)
    elif command == '--casyco':
        message = analyze_images(args, casyco)
        print(message)
    elif command == '--cflatco':
        message = analyze_images(args, cflatco)
        print(message)
    elif command == '--cvarcoii':
        message = analyze_images(args, cvarcoii)
        print(message)
    elif command == '--centropy':
        message = analyze_images(args, centropy)
        print(message)

    # Convolution
    elif command == '--sedgesharp':
        transform_image(args, edge_sharpening)

    elif command == '--orosenfeld':
        transform_image(args, orosenfeld)

    # Task 3
    elif command == '--dilation':
        transform_image(args, dilation)
    elif command == '--erosion':
        transform_image(args, erosion)
    elif command == '--opening':
        transform_image(args, opening)
    elif command == '--closing':
        transform_image(args, closing)
    elif command == '--hmt':
        transform_image(args, hmt)
    
    elif command == '--m3':
        transform_image(args, m3)
    elif command == '--regions':
        transform_image(args, region_growing)

    # Task 4
    elif command == '--dft-test':
        transform_image(args, dft2d_and_back)
    elif command == '--fft-test':
        transform_image(args, fft2d_and_back)
    elif command == '--fft':
        transform_image(args, fft_img)
    elif command == '--low-pass':
        transform_image(args, low_pass_filter)
    elif command == '--high-pass':
        transform_image(args, high_pass_filter)
    elif command == '--band-pass':
        transform_image(args, band_pass_filter)
    
    else:
        raise UnknownArgumentError("Unknown command: " + command)
