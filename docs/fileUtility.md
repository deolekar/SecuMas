# File Utility

Utilities to convert market data vendor feed files

## Bloomberg

### CSV -> BBG

Utility for Bloomberg Back Office feed file conversion.
</br>

#### Input

Pipe delimited CSV with first row as header. [Sample](https://github.com/deolekar/SecuMas/blob/master/Sample/inputcsv_to_bbg.csv)

#### Output

BBG file at specified path.

```py
import SecuMas

SecuMas.bbgbo.fromcsv('path/to/inputcsv_to_bbg.csv','path/to/output_bbg_bo.dif')
```
