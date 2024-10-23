from typing import Dict

def replace_multiple_substrings(s: str, replacements: Dict[str, str]) -> str:
    """
    Replace multiple substrings with corresponding replacements.

    Parameters
    ----------
    s : str
        The input string.
    replacements : Dict[str, str]
        A dictionary where keys are substrings to be replaced and values are the corresponding replacements.

    Returns
    -------
    str
        The string with multiple substrings replaced.

    Examples
    --------
    >>> replace_multiple_substrings("hello world", {"hello": "hi", "world": "earth"})
    'hi earth'
    >>> replace_multiple_substrings("a.b.c", {".": "-"})
    'a-b-c'
    """
    for old, new in replacements.items():
        s = s.replace(old, new)
    return s
