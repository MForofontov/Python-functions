def contains_substring(s: str, substring: str) -> bool:
    """
    Check if a string contains a specified substring.

    Parameters
    ----------
    s : str
        The input string.
    substring : str
        The substring to check for.

    Returns
    -------
    bool
        True if the string contains the substring, False otherwise.

    Examples
    --------
    >>> contains_substring("hello world", "world")
    True
    >>> contains_substring("hello world", "there")
    False
    """
    return substring in s
