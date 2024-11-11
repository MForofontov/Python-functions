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
    """
    return re.sub(pattern, '', string)