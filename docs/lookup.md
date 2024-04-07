# Lookup

A module to parse, validate and lookup codes eg CFI, GICS etc..

## GICS

Check if GICS is valid. This checks the length, format. Returns back GICS Classification, if valid.

```py
import SecuMas

classification = SecuMas.gics('45203020')
print(classification.level(1).name) #Information Technology
print(classification.level(2).name) #Technology Hardware & Equipment
print(classification.level(3).name) #Electronic Equipment, Instruments & Components
print(classification.level(4).name) #Electronic Manufacturing Services

print(classification.sector.name) #Information Technology
print(classification.industry_group.name) #Technology Hardware & Equipment
print(classification.industry.name) #Electronic Equipment, Instruments & Components
print(classification.sub_industry.name) #Electronic Manufacturing Services

print(classification.sub_industry.description) #Producers of electronic equipment mainly for the OEM (Original Equipment Manufacturers) markets.

print(classification.sector.code) #45
print(classification.industry_group.code) #4520
print(classification.industry.code) #452030
print(classification.sub_industry.code) #45203020
```

</br>
By default latest [GICS mapping](https://github.com/deolekar/SecuMas/tree/master/SecuMas/definitions) is referred. Below snippet point to previous version of the mapping.

```py
#classification = SecuMas.gics(<gics_code>, <date>)
classification = SecuMas.gics('45203020', '20180929')
```

</br>
