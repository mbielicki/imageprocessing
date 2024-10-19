$BoxSize = 7

Write-Output "`n=== Testing noise removal for box size = $BoxSize ===`n"


Write-Output "`n=== median ===`n"

python imageprocessing.py --median --input=data/lenac_normal3.bmp --output=data/median-$BoxSize.bmp

python imageprocessing.py --mse --reference=data/lenac.bmp --input=data/median-$BoxSize.bmp 
python imageprocessing.py --pmse --reference=data/lenac.bmp --input=data/median-$BoxSize.bmp 
python imageprocessing.py --snr --reference=data/lenac.bmp --input=data/median-$BoxSize.bmp 
python imageprocessing.py --psnr --reference=data/lenac.bmp --input=data/median-$BoxSize.bmp 
python imageprocessing.py --md --reference=data/lenac.bmp --input=data/median-$BoxSize.bmp 


Write-Output "`n=== gmean ===`n"


python imageprocessing.py --gmean --input=data/lenac_normal3.bmp --output=data/gmean-$BoxSize.bmp

python imageprocessing.py --mse --reference=data/lenac.bmp --input=data/gmean-$BoxSize.bmp 
python imageprocessing.py --pmse --reference=data/lenac.bmp --input=data/gmean-$BoxSize.bmp 
python imageprocessing.py --snr --reference=data/lenac.bmp --input=data/gmean-$BoxSize.bmp 
python imageprocessing.py --psnr --reference=data/lenac.bmp --input=data/gmean-$BoxSize.bmp 
python imageprocessing.py --md --reference=data/lenac.bmp --input=data/gmean-$BoxSize.bmp 
