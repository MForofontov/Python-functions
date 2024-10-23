def starts_with(s: str, prefix: str) -> bool:
    """
    Check if a string starts with a specified prefix.

    Parameters
    ----------
    s : str
        The input string.
    prefix : str
        The prefix to check.

    Returns
    -------
    bool
        True if the string starts with the prefix, False otherwise.

    Examples
    --------
    >>> starts_with("hello world", "hello")
    True
    >>> starts_with("hello world", "world")
    False
    """
    return s.startswith(prefix)
