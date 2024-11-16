$Images = "lenac"

foreach ($Image in $Images) {
    for ($Kernel = 0; $Kernel -lt 3; $Kernel++) {
        python imageprocessing.py --sedgesharp --input=./data/$Image.bmp --output=./data/conv/$Image-sharp-fix-$Kernel.bmp --kernel=$Kernel
    }
}