def rjust_string(s: str, width: int, fillchar: str = ' ') -> str:
    """
    Right-justify a string in a field of a specified width.

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
        The right-justified string.

    Examples
    --------
    >>> rjust_string("hello", 10)
    '     hello'
    >>> rjust_string("hello", 10, '-')
    '-----hello'
    """
    return s.rjust(width, fillchar)
