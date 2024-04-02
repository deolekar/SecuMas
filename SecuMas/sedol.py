import random

# the letters allowed in an SEDOL
_characterSet = '0123456789 BCD FGH JKLMN PQRST VWXYZ'

def stripe(identifier):
    """Stripe unwanted symbols & spaces"""
    return ''.join(x for x in identifier if x not in ' ').strip().upper()

def get_check_digit(identifier):
    """Calculate the check digit of SEDOL."""
    weights = (1, 3, 1, 7, 3, 9)
    s = sum(w * _characterSet.index(n) for w, n in zip(weights, identifier))
    return str((10 - s) % 10)

def validate(identifier):
    """Check if SEDOL is valid. This checks the length and check digit."""
    identifier = stripe(identifier)
    if not all(x in _characterSet for x in identifier):
        return 'Invalid Format'
    if len(identifier) != 7:
        return 'Incorrect Length'
    if get_check_digit(identifier[:-1]) != identifier[-1]:
        return 'Incorrect Checkdigit'
    return identifier

def dummy(number):
    """Generate dummy SEDOLs."""
    sedols = []
    number = int(number)
    for n in range(number):
        identifier = 'BH' + str(random.randint(1000,9999))
        sedol = identifier + get_check_digit(identifier) 
        sedols.append(sedol)
    return sedols
