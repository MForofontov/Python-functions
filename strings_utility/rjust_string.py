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
    if not isinstance(s, str):
        raise TypeError("The first argument must be a string.")
    if not isinstance(width, int):
        raise TypeError("The second argument must be an integer.")
    if not isinstance(fillchar, str) or len(fillchar) != 1:
        raise TypeError("The third argument must be a single character string.")
    return s.rjust(width, fillchar)
