import random

# the letters allowed in an ISIN
_characterSet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def stripe(identifier):
    """Stripe unwanted symbols & spaces"""
    return ''.join(x for x in identifier if x not in ' ').strip().upper()

def get_check_digit(identifier):
    """Calculate the check digit of ISIN."""
    # convert to numeric first, then double some, then sum individual digits
    identifier = ''.join(str(_characterSet.index(n)) for n in identifier)
    identifier = ''.join(
        str((2, 1)[i % 2] * int(n)) for i, n in enumerate(reversed(identifier)))
    return str((10 - sum(int(n) for n in identifier)) % 10)

def validate(identifier):
    """Check if ISIN id valid. This checks the length and check digit."""
    identifier = stripe(identifier)
    if not all(x in _characterSet for x in identifier):
        return 'Invalid Format'
    if len(identifier) != 12:
        return 'Incorrect Length'
    """if identifier[:2] not in _country_codes:
        raise InvalidComponent()"""
    if get_check_digit(identifier[:-1]) != identifier[-1]:
        return 'Incorrect Checkdigit'
    return identifier

def dummy(number):
    """Generate dummy ISINs."""
    isins = []
    number = int(number)
    for n in range(number):
        identifier = 'IN' + str(random.randint(100000000,999999999))
        isin = identifier + get_check_digit(identifier) 
        isins.append(isin)
    return isins
