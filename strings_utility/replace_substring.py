def replace_substring(s: str, old: str, new: str) -> str:
    """
    Replace all occurrences of a substring with another substring.

    Parameters
    ----------
    s : str
        The input string.
    old : str
        The substring to be replaced.
    new : str
        The substring to replace with.

    Returns
    -------
    str
        The string with all occurrences of the old substring replaced by the new substring.

    Examples
    --------
    >>> replace_substring("hello world", "world", "there")
    'hello there'
    >>> replace_substring("a.b.c", ".", "-")
    'a-b-c'
    """
    return s.replace(old, new)
