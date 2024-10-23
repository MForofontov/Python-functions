def remove_whitespace(s: str) -> str:
    """
    Remove all whitespace characters from a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with all whitespace characters removed.

    Examples
    --------
    >>> remove_whitespace("hello world")
    'helloworld'
    >>> remove_whitespace(" a b c ")
    'abc'
    """
    return ''.join(s.split())
