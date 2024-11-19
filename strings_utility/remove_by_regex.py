import re

def remove_by_regex(string: str, pattern: str) -> str:
    """
    Remove all occurrences of a pattern from a string.

    Parameters
    ----------
    string : str
        The string to remove the pattern from.
    pattern : str
        The regex pattern to remove from the string.

    Returns
    -------
    str
        The string with all occurrences of the pattern removed.

    Raises
    ------
    TypeError
        If string is not a string or pattern is not a string.
    """
    if not isinstance(string, str):
        raise TypeError("string must be a string")
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a string")

    return re.sub(pattern, '', string)