from typing import List

def split_string(s: str, delimiter: str = ' ') -> List[str]:
    """
    Split a string by a specified delimiter.

    Parameters
    ----------
    s : str
        The input string.
    delimiter : str, optional
        The delimiter to split the string by (default is space).

    Returns
    -------
    List[str]
        A list of substrings.

    Examples
    --------
    >>> split_string("hello world")
    ['hello', 'world']
    >>> split_string("a,b,c", delimiter=",")
    ['a', 'b', 'c']
    """
    return s.split(delimiter)
