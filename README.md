# Introduction

This Repo is for Securities Master Python custom package built.

```batch
pip install SecuMas
```

Examples:

```python
import SecuMas

''' Validate (ISIN)'''
print (SecuMas.isin.validate('IN8081309367'))

''' Generate Dummy ISINs (development usecase)'''
print (SecuMas.isin.dummy(5))

```

# Package documentation

> [Documentation](https://www.secumas.dev/)

# Code contributions

Improvements to SecuMas are most welcome. Integrating contributions will be done on a best-effort basis and can be made easier if the following are considered:

Contributions are made as GitHub pull requests.

Submitted contributions will often be reformatted and sometimes restructured for consistency with other parts.

Contributions will be acknowledged in the release notes.

Contributions should add or update a copyright statement if you feel the contribution is significant.

All contribution should be made with compatible applicable copyright.

It is not needed to modify the README.md, it will be updated on release.

All code should be well tested and achieve 100% code coverage.
