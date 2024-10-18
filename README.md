# Example commands:

## Elementary operations

```shell
python imageprocessing.py --negative --input=data/lenac.bmp --output=negative-lenac.bmp
python imageprocessing.py --brightness --strength=100 --input=data/lenac.bmp --output=bright-lenac.bmp
python imageprocessing.py --contrast --strength=3 --input=data/lenac.bmp --output=contrast-lenac.bmp
```

## Geometric operations

```shell
python imageprocessing.py --enlarge --proportion=30 --input=data/interpolation_test.bmp
python imageprocessing.py --hflip --input=data/lenac.bmp
```

## Noise filtering

```shell
python imageprocessing.py --median --input=data/lenac_normal3.bmp --output=data/output-median.bmp
python imageprocessing.py --gmean --input=data/lenac_normal3.bmp --output=data/output-gmean.bmp
```

## Similarity

```shell
python imageprocessing.py --mse --input=data/output-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --pmse --input=data/output-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --snr --input=data/output-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --psnr --input=data/output-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --md --input=data/output-median.bmp --reference=data/lenac.bmp
```
