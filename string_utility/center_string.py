def center_string(s: str, width: int, fillchar: str = ' ') -> str:
    """
    Center a string in a field of a specified width.

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
        The centered string.

    Examples
    --------
    >>> center_string("hello", 11)
    '   hello   '
    >>> center_string("hello", 11, '-')
    '---hello---'
    """
    return s.center(width, fillchar)
