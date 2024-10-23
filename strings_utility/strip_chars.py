def strip_chars(s: str, chars: str) -> str:
    """
    Strip specified characters from both ends of a string.

    Parameters
    ----------
    s : str
        The input string.
    chars : str
        The characters to strip.

    Returns
    -------
    str
        The string with specified characters stripped from both ends.

    Examples
    --------
    >>> strip_chars("...hello...", ".")
    'hello'
    >>> strip_chars("xyzhellozyx", "xyz")
    'hello'
    """
    return s.strip(chars)
