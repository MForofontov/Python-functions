def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    bool
        True if the string is a palindrome, False otherwise.

    Examples
    --------
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    """
    return s == s[::-1]