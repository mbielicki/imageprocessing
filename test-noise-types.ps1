$fileName = "g-uniform1"

Write-Output "`n=== Testing noise removal for $fileName ===`n"


Write-Output "`n=== median ===`n"

python imageprocessing.py --median --input=data/$fileName.bmp --output=data/median-$fileName.bmp

python imageprocessing.py --mse --reference=data/lena.bmp --input=data/median-$fileName.bmp 
python imageprocessing.py --pmse --reference=data/lena.bmp --input=data/median-$fileName.bmp 
python imageprocessing.py --snr --reference=data/lena.bmp --input=data/median-$fileName.bmp 
python imageprocessing.py --psnr --reference=data/lena.bmp --input=data/median-$fileName.bmp 
python imageprocessing.py --md --reference=data/lena.bmp --input=data/median-$fileName.bmp 


Write-Output "`n=== gmean ===`n"


python imageprocessing.py --gmean --input=data/$fileName.bmp --output=data/gmean-$fileName.bmp

python imageprocessing.py --mse --reference=data/lena.bmp --input=data/gmean-$fileName.bmp 
python imageprocessing.py --pmse --reference=data/lena.bmp --input=data/gmean-$fileName.bmp 
python imageprocessing.py --snr --reference=data/lena.bmp --input=data/gmean-$fileName.bmp 
python imageprocessing.py --psnr --reference=data/lena.bmp --input=data/gmean-$fileName.bmp 
python imageprocessing.py --md --reference=data/lena.bmp --input=data/gmean-$fileName.bmp 

