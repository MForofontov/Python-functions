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
    return s.lstrip(chars)
