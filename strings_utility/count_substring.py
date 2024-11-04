def count_substring(s: str, substring: str) -> int:
    """
    Count the number of non-overlapping occurrences of a substring in a string.

    Parameters
    ----------
    s : str
        The input string.
    substring : str
        The substring to count.

    Returns
    -------
    int
        The number of non-overlapping occurrences of the substring.

    Examples
    --------
    >>> count_substring("hello world", "o")
    2
    >>> count_substring("ababab", "ab")
    3
    """
    if not isinstance(s, str):
        raise TypeError("The input must be a string.")
    return s.count(substring)
