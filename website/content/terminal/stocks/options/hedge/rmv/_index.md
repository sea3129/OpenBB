```
usage: rmv [-o OPTION [OPTION ...]] [-a] [-h]

Remove one of the options to be shown in the hedge.

optional arguments:
  -o OPTION [OPTION ...], --option OPTION [OPTION ...]
                        index of the option to remove
  -a, --all             remove all of the options
  -h, --help            show this help message
```

Example:
```
2022 May 10, 09:32 (๐ฆ) /stocks/options/hedge/ $ rmv Option A
          Current Option Positions           
โโโโโโโโณโโโโโโโณโโโโโโโโโณโโโโโโโโโโโโโโโโโโโโโ
โ Type โ Hold โ Strike โ Implied Volatility โ
โกโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโฉ
โ Call โ Long โ 155.00 โ 0.06               โ
โโโโโโโโดโโโโโโโดโโโโโโโโโดโโโโโโโโโโโโโโโโโโโโโ
```