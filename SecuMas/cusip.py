import random

# the letters allowed in an CUSIP
_characterSet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*@#'

def stripe(identifier):
    """Stripe unwanted symbols & spaces"""
    return ''.join(x for x in identifier if x not in ' ').strip().upper()

def get_check_digit(identifier):
    """Calculate the check digit of CUSIP."""
    # convert to numeric first, then sum individual digits
    identifier = ''.join(
        str((1, 2)[i % 2] * _characterSet.index(n)) for i, n in enumerate(identifier))
    return str((10 - sum(int(n) for n in identifier)) % 10)

def validate(identifier):
    """Check if CUSIP id valid. This checks the length and check digit."""
    identifier = stripe(identifier)
    if not all(x in _characterSet for x in identifier):
        return 'Invalid Format'
    if len(identifier) != 9:
        return 'Incorrect Length'
    """if identifier[:2] not in _country_codes:
        raise InvalidComponent()"""
    if get_check_digit(identifier[:-1]) != identifier[-1]:
        return 'Incorrect Checkdigit'
    return identifier

def dummy(number):
    """Generate dummy CUSIPs."""
    cusips = []
    number = int(number)
    for n in range(number):
        identifier = '91A' + str(random.randint(10000,99999))
        cusip = identifier + get_check_digit(identifier) 
        cusips.append(cusip)
    return cusips
