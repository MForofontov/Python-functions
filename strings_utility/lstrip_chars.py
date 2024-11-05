def lstrip_chars(s: str, chars: str) -> str:
    """
    Strip specified characters from the left end of a string.

    Parameters
    ----------
    s : str
        The input string.
    chars : str
        The characters to strip.

    Returns
    -------
    str
        The string with specified characters stripped from the left end.

    Examples
    --------
    >>> lstrip_chars("...hello...", ".")
    'hello...'
    >>> lstrip_chars("xyzhellozyx", "xyz")
    'hellozyx'
    """
    if not isinstance(s, str):
        raise TypeError("The input string must be a string.")
    if not isinstance(chars, str):
        raise TypeError("The characters to strip must be a string.")
    return s.lstrip(chars)
