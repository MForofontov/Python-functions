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
    if not isinstance(s, str):
        raise TypeError("The input must be a string.")
    return ''.join(s.split())
