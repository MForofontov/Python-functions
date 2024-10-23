def truncate_string_range(s: str, start: int, end: int) -> str:
    """
    Truncate a string from a specified start index to an end index.

    Parameters
    ----------
    s : str
        The input string.
    start : int
        The start index for truncation (inclusive).
    end : int
        The end index for truncation (exclusive).

    Returns
    -------
    str
        The truncated string.

    Examples
    --------
    >>> truncate_string_range("hello world", 0, 5)
    'hello'
    >>> truncate_string_range("hello world", 6, 11)
    'world'
    >>> truncate_string_range("abc", 1, 5)
    'bc'
    """
    return s[start:end]
