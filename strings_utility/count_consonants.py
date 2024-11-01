def count_consonants(s: str) -> int:
    """
    Count the number of consonants in a string (English).

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    int
        The number of consonants in the input string.

    Examples
    --------
    >>> count_consonants("hello")
    3
    >>> count_consonants("world")
    4
    """
    if not isinstance(s, str):
        raise TypeError("The input must be a string.")
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in s if char in consonants)
