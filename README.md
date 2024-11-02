# Example commands:

## Elementary operations

```shell
python imageprocessing.py --negative --input=data/lenac.bmp --output=data/negative-lenac.bmp
python imageprocessing.py --brightness --strength=100 --input=data/lenac.bmp --output=data/bright-lenac.bmp
python imageprocessing.py --contrast --strength=3 --input=data/lenac.bmp --output=data/contrast-lenac.bmp
```

## Geometric operations

```shell
python imageprocessing.py --hflip --input=data/lenac.bmp --output=data/hflip-lenac.bmp
python imageprocessing.py --vflip --input=data/lenac.bmp --output=data/vflip-lenac.bmp
python imageprocessing.py --dflip --input=data/lenac.bmp --output=data/dflip-lenac.bmp
python imageprocessing.py --enlarge --proportion=1.5 --input=data/interpolation_test.bmp --output=data/large-lenac.bmp
python imageprocessing.py --shrink --proportion=0.6  --input=data/lenac.bmp --output=data/shrink-lenac.bmp
```

## Noise filtering

```shell
python imageprocessing.py --median --input=data/lenac_normal3.bmp --output=data/lenac_normal3-median.bmp
python imageprocessing.py --gmean --input=data/lenac_normal3.bmp --output=data/lenac_normal3-gmean.bmp
```

## Similarity

```shell
python imageprocessing.py --mse --input=data/lenac_normal3-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --pmse --input=data/lenac_normal3-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --snr --input=data/lenac_normal3-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --psnr --input=data/lenac_normal3-median.bmp --reference=data/lenac.bmp
python imageprocessing.py --md --input=data/lenac_normal3-median.bmp --reference=data/lenac.bmp
```

## Task 2

### Histogram

```shell
python imageprocessing.py --histogram --input=data/lena.bmp --output=data/hist/h-lena.bmp
```

### hpower

```shell
python imageprocessing.py --hpower --input=data/lena.bmp --output=data/hist/lena-hpower.bmp
python imageprocessing.py --histogram --input=data/hist/lena-hpower.bmp --output=data/hist/h-lena-hpower.bmp
```

### Characteristics

```shell
python imageprocessing.py --cmean --input=data/lena.bmp
python imageprocessing.py --cvariance --input=data/lena.bmp
python imageprocessing.py --cstdev --input=data/lena.bmp
python imageprocessing.py --cvarcoi --input=data/lena.bmp
```
