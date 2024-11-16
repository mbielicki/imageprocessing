$Images = "lena", "camera", "pentagon"

foreach ($Image in $Images) {
    python imageprocessing.py --hpower --input=data/$Image.bmp --output=data/hist/$Image-hpower.bmp --gmin=10
    python imageprocessing.py --histogram --input=data/$Image.bmp --output=data/hist/$Image-h.bmp
    python imageprocessing.py --histogram --input=data/hist/$Image-hpower.bmp --output=data/hist/$Image-hpower-h.bmp

}

$Image = "lenac"
$Colors = "r", "g", "b"

python imageprocessing.py --hpower --input=data/$Image.bmp --output=data/hist/$Image-hpower.bmp --gmin=10 --gmax=240

foreach ($Color in $Colors) {
    python imageprocessing.py --histogram --input=data/$Image.bmp --output=data/hist/$Image-h-$Color.bmp --channel=$Color
    python imageprocessing.py --histogram --input=data/hist/$Image-hpower.bmp --output=data/hist/$Image-hpower-h-$Color.bmp --channel=$Color
}