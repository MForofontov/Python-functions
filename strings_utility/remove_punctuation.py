import string

def remove_punctuation(s: str) -> str:
    """
    Remove all punctuation characters from a string.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The string with all punctuation characters removed.

    Examples
    --------
    >>> remove_punctuation("hello, world!")
    'hello world'
    >>> remove_punctuation("a.b,c!")
    'abc'
    """
    if not isinstance(s, str):
        raise TypeError("The input must be a string.")
    return s.translate(str.maketrans('', '', string.punctuation))
