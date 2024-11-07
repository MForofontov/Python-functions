from typing import List

def join_strings(strings: List[str], delimiter: str = ' ') -> str:
    """
    Join a list of strings into a single string with a specified delimiter.

    Parameters
    ----------
    strings : List[str]
        The list of strings to join.
    delimiter : str, optional
        The delimiter to join the strings with (default is space).

    Returns
    -------
    str
        The joined string.

    Examples
    --------
    >>> join_strings(['hello', 'world'])
    'hello world'
    >>> join_strings(['a', 'b', 'c'], delimiter=",")
    'a,b,c'
    """
    if not isinstance(strings, list) and not all(isinstance(item, str) for item in strings):
        raise TypeError("All elements in the list must be strings.")
    if not isinstance(delimiter, str):
        raise TypeError("The delimiter must be a string.")
    return delimiter.join(strings)