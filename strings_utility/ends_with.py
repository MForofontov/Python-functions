def ends_with(s: str, suffix: str) -> bool:
    """
    Check if a string ends with a specified suffix.

    Parameters
    ----------
    s : str
        The input string.
    suffix : str
        The suffix to check.

    Returns
    -------
    bool
        True if the string ends with the suffix, False otherwise.

    Examples
    --------
    >>> ends_with("hello world", "world")
    True
    >>> ends_with("hello world", "hello")
    False
    """
    if not isinstance(s, str):
        raise TypeError("The input must be a string.")
    return s.endswith(suffix)
