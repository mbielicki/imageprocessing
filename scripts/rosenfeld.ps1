$Images = "lena", "camera", "pentagon", "lenac"
$P_values = 1, 2, 4, 8, 16

foreach ($Image in $Images) {
    foreach ($P_val in $P_values) {
        
        python imageprocessing.py --orosenfeld --input=./data/$Image.bmp --output=./data/conv/rosenfeld/$Image-rosenfeld-$P_val.bmp --P=$P_val
    }
    
}