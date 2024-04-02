# Identifier

A module to parse, validate and reformat standard identifiers and codes in different formats.

## ISIN

Check if ISIN is valid. This checks the length, format and check digit. Returns back ISIN, if valid.

```py
print (SecuMas.isin.validate('IN8081309367'))
```

</br>
Generate check digit. Input expected 11 character string.

```py
print (SecuMas.isin.get_check_digit('IN808130936'))
```

</br>
Generate dummy ISINs (development usecase). Output as list.

```py
print (SecuMas.isin.dummy(3))
```

## CUSIP

Check if CUSIP is valid. This checks the length, format and check digit. Returns back CUSIP, if valid.

```py
print (SecuMas.cusip.validate('H42097107'))
```

</br>
Generate check digit. Input expected 8 character string.

```py
print (SecuMas.cusip.get_check_digit('H4209710'))
```

</br>
Generate dummy CUSIPs (development usecase). Output as list.

```py
print (SecuMas.cusip.dummy(3))
```

## SEDOL

Check if SEDOL is valid. This checks the length, format and check digit. Returns back SEDOL, if valid.

```py
print (SecuMas.sedol.validate('0870612'))
```

</br>
Generate check digit. Input expected 6 character string.

```py
print (SecuMas.sedol.get_check_digit('087061'))
```

</br>
Generate dummy SEDOLs (development usecase). Output as list.

```py
print (SecuMas.sedol.dummy(3))
```
