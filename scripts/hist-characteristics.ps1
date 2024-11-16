$Image = "camera"

Write-Output "`n=== Hist characteristics for image = $Image ===`n"

python imageprocessing.py --cmean --input=data/$Image.bmp
python imageprocessing.py --cvariance --input=data/$Image.bmp
python imageprocessing.py --cstdev --input=data/$Image.bmp
python imageprocessing.py --cvarcoi --input=data/$Image.bmp
python imageprocessing.py --casyco --input=data/$Image.bmp
python imageprocessing.py --cflatco --input=data/$Image.bmp
python imageprocessing.py --cvarcoii --input=data/$Image.bmp
python imageprocessing.py --centropy --input=data/$Image.bmp
