def reverse_string(s: str) -> str:
    """
    Reverse the characters in a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with characters in reverse order.

    Examples
    --------
    >>> reverse_string("hello")
    'olleh'
    """
    return s[::-1]