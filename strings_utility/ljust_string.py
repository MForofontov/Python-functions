def ljust_string(s: str, width: int, fillchar: str = ' ') -> str:
    """
    Left-justify a string in a field of a specified width.

    Parameters
    ----------
    s : str
        The input string.
    width : int
        The width of the field.
    fillchar : str, optional
        The character to fill the field with (default is space).

    Returns
    -------
    str
        The left-justified string.

    Examples
    --------
    >>> ljust_string("hello", 10)
    'hello     '
    >>> ljust_string("hello", 10, '-')
    'hello-----'
    """
    return s.ljust(width, fillchar)
