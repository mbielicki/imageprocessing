help_message = """
Image processing CLI:
    python imageprocessing.py --command [--argument=value [...]]
    
Available commands:

Elementary operations:
--negative: Invert the colors of the image
    --input: Input image file
    --output: Output image file

--brightness: Adjust the brightness of the image
    --input: Input image file
    --output: Output image file
    --strength: Brightness adjustment value (integer)

--contrast: Adjust the contrast of the image
    --input: Input image file
    --output: Output image file
    --strength: Contrast adjustment value (float)

Geometric operations:
--hflip: Flip the image horizontally
    --input: Input image file
    --output: Output image file

--vflip: Flip the image vertically
    --input: Input image file
    --output: Output image file

--dflip: Flip the image diagonally
    --input: Input image file
    --output: Output image file

--enlarge: Enlarge the image
    --input: Input image file
    --output: Output image file
    --proportion: Enlargement proportion (float)

--shrink: Shrink the image
    --input: Input image file
    --output: Output image file
    --proportion: Shrinkage proportion (float)

Noise removal:
--median: Apply median filter to the image
    --input: Input image file
    --output: Output image file

--gmean: Apply geometric mean filter to the image
    --input: Input image file
    --output: Output image file

Image similarity:
--mse: Calculate mean square error between two images
    --input: Input image file
    --reference: Reference image file

--pmse: Calculate peak mean square error between two images
    --input: Input image file
    --reference: Reference image file

--snr: Calculate signal to noise ratio between two images
    --input: Input image file
    --reference: Reference image file

--psnr: Calculate peak signal to noise ratio between two images
    --input: Input image file
    --reference: Reference image file

--md: Calculate maximum difference between two images
    --input: Input image file
    --reference: Reference image file
"""