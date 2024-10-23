def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with the first letter of each word capitalized.

    Examples
    --------
    >>> capitalize_words("hello world")
    'Hello World'
    """
    return s.title()
