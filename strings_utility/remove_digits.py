def remove_digits(s: str) -> str:
    """
    Remove all numerical digits from a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with all numerical digits removed.

    Examples
    --------
    >>> remove_digits("abc123")
    'abc'
    >>> remove_digits("12345")
    ''
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return ''.join(char for char in s if not char.isdigit())
