def truncate_string_range(s: str, start: int, end: int) -> str:
    """
    Truncate a string to a specified range.

    Parameters
    ----------
    s : str
        The input string.
    start : int
        The starting index of the range.
    end : int
        The ending index of the range.

    Returns
    -------
    str
        The truncated string.

    Raises
    ------
    TypeError
        If the input string is not a string or if the start or end indices are not integers.
    ValueError
        If the start or end indices are out of range.

    Examples
    --------
    >>> truncate_string_range("hello world", 0, 5)
    'hello'
    >>> truncate_string_range("python programming", 7, 18)
    'programming'
    >>> truncate_string_range("1234567890", 2, 5)
    '345'
    >>> truncate_string_range("truncate", 0, 4)
    'trun'
    """
    if not isinstance(s, str):
        raise TypeError("The input string must be a string.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("The start and end indices must be integers.")
    if start < 0 or end > len(s) or start > end:
        raise ValueError("The start and end indices are out of range.")
    
    return s[start:end]
