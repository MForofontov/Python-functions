def remove_non_alphanumeric(s: str) -> str:
    """
    Remove all non-alphanumeric characters from a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with all non-alphanumeric characters removed.

    Examples
    --------
    >>> remove_non_alphanumeric("abc123!@#")
    'abc123'
    >>> remove_non_alphanumeric("!@#$%^&*()")
    ''
    """
    return ''.join(char for char in s if char.isalnum())
