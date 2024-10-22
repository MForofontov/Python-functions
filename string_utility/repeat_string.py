def repeat_string(s: str, n: int) -> str:
    """
    Repeat a string a specified number of times.

    Parameters
    ----------
    s : str
        The input string.
    n : int
        The number of times to repeat the string.

    Returns
    -------
    str
        The repeated string.

    Examples
    --------
    >>> repeat_string("hello", 3)
    'hellohellohello'
    >>> repeat_string("abc", 2)
    'abcabc'
    """
    return s * n
