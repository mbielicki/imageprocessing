from typing import Callable
import numpy as np
from exceptions import ComparisonError, MissingArgumentError
from img_file_to_arr import img_file_to_arr

type ImageComparator = Callable[[dict, np.ndarray, np.ndarray], str]
def compare_images(args: dict, func: ImageComparator) -> str:
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

    if input_im.shape != ref_im.shape:
        raise ComparisonError("Input and reference image must have the same shape.")

    return func(args, input_im, ref_im)

type ImageAnalyzer = Callable[[dict, np.ndarray], str]
def analyze_images(args: dict, func: ImageAnalyzer) -> str:
    try:
        input_file = args['--input']
    except KeyError:
        raise MissingArgumentError("No input file given.")
    
    input_im = img_file_to_arr(input_file)

    
    return func(args, input_im)
