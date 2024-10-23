def truncate_string(s: str, length: int) -> str:
    """
    Truncate a string to a specified length.

    Parameters
    ----------
    s : str
        The input string.
    length : int
        The length to truncate the string to.

    Returns
    -------
    str
        The truncated string.

    Examples
    --------
    >>> truncate_string("hello world", 5)
    'hello'
    >>> truncate_string("abc", 5)
    'abc'
    """
    return s[:length]
