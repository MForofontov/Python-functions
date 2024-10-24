def count_consonants(s: str) -> int:
    """
    Count the number of consonants in a string.

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
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)
