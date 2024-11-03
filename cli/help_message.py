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
    --strength: Brightness adjustment value (integer, -255 to 255)

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
    --proportion: Enlargement proportion (float, > 1)

--shrink: Shrink the image
    --input: Input image file
    --output: Output image file
    --proportion: Shrinkage proportion (float, < 1)

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
    
Histogram:
--histogram: Show the histogram of the image
    --input: Input image file
    --output: Histogram file

--hpower: Apply the Power 2/3 final probability density function
    --input: Input image file
    --output: Output image file

Characteristics:
--cmean: Calculate the mean of the image
    --input: Input image file

--cvariance: Calculate the variance of the image
    --input: Input image file

--cstdev: Calculate the standard deviation of the image
    --input: Input image file

--cvarcoi: Calculate the variance coefficient of the image
    --input: Input image file

--casyco: Calculate the asymmetry coefficient of the image
    --input: Input image file

--cflatco: Calculate the flatness coefficient of the image
    --input: Input image file

--cvarcoii: Calculate the variance coefficient II of the image
    --input: Input image file

--centropy: Calculate the entropy of the image
    --input: Input image file

Convolution:
--sedgesharp: Apply the edge sharp filter to the image
    --input: Input image file
    --output: Output image file
    --kernel: Kernel type - allowed values: (0: optimized, 1, 2)

--orosenfeld: Apply the Rosenfeld filter to the image
    --input: Input image file
    --output: Output image file
    --P: P value - allowed values: (1, 2, 4, 8, 16)
"""