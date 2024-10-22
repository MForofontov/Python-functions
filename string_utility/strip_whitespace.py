def strip_whitespace(s: str) -> str:
    """
    Strip leading and trailing whitespace from a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with leading and trailing whitespace removed.

    Examples
    --------
    >>> strip_whitespace("  hello  ")
    'hello'
    >>> strip_whitespace("  abc  ")
    'abc'
    """
    return s.strip()
