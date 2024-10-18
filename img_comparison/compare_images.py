from exceptions import MissingArgumentError
from img_file_to_arr import img_file_to_arr

def compare_images(args, func) -> str:
    try:
        input_file = args['--input']
    except KeyError:
        raise MissingArgumentError("No input file given.")
    
    try:
        ref_file = args['--reference']
    except KeyError:
        raise MissingArgumentError("No reference file given.")
    
    input_im = img_file_to_arr(input_file)
    ref_im = img_file_to_arr(ref_file)

    return func(args, input_im, ref_im)

