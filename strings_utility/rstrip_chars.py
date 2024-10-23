def rstrip_chars(s: str, chars: str) -> str:
    """
    Strip specified characters from the right end of a string.

    Parameters
    ----------
    s : str
        The input string.
    chars : str
        The characters to strip.

    Returns
    -------
    str
        The string with specified characters stripped from the right end.

    Examples
    --------
    >>> rstrip_chars("...hello...", ".")
    '...hello'
    >>> rstrip_chars("xyzhellozyx", "xyz")
    'xyzhello'
    """
    return s.rstrip(chars)
