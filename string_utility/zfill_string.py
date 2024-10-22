def zfill_string(s: str, width: int) -> str:
    """
    Pad a numeric string on the left with zeros to fill a specified width.

    Parameters
    ----------
    s : str
        The input string.
    width : int
        The width to pad the string to.

    Returns
    -------
    str
        The string padded with zeros on the left to the specified width.

    Examples
    --------
    >>> zfill_string("42", 5)
    '00042'
    >>> zfill_string("-42", 5)
    '-0042'
    """
    return s.zfill(width)
