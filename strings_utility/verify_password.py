import re
from typing import List, Callable

def verify_password(password: str, custom_checks: List[Callable[[str], bool]] = []) -> bool:
    """
    Verify if a password meets the following criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase characters
    - Contains at least one numerical digit
    - Contains at least one special character (e.g., @, #, $, etc.)
    - Passes all custom checks provided

    Parameters
    ----------
    password : str
        The password to verify.
    custom_checks : List[Callable[[str], bool]], optional
        A list of custom check functions that take the password as input and return a boolean.

    Returns
    -------
    bool
        True if the password meets all criteria, False otherwise.

    Examples
    --------
    >>> verify_password("Password123!")
    True
    >>> verify_password("password")
    False
    >>> verify_password("PASSWORD123")
    False
    >>> verify_password("Pass123")
    False
    >>> custom_check = lambda p: 'example' in p
    >>> verify_password("Password123!example", custom_checks=[custom_check])
    True
    >>> verify_password("Password123!", custom_checks=[custom_check])
    False
    """
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase characters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False

    # Check if the password contains at least one numerical digit
    if not re.search(r'\d', password):
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[@#$%^&+=]', password):
        return False

    # Check custom rules
    for check in custom_checks:
        if not check(password):
            return False

    return True

