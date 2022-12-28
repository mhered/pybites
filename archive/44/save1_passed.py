# use one or more Standard Library modules
import string
import secrets

def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    """
    Generate and return a random license key containing
    upper case characters and digits.

    Example with default "parts" and "chars_per_part"
    being 4 and 8: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    If parts = 3 and chars_per_part = 4 a random license
    key would look like this: 54N8-I70K-2JZ7
    """
    alphabet = string.ascii_uppercase + string.digits
    return '-'.join(''.join(secrets.choice(alphabet) for j in range(chars_per_part)) for i in range(parts))

print(gen_key(4,8))