from typing import Union
import re

def search_string_by_regex(pattern: str, string: str) -> Union[str, None]:
    """
    Searches for a regex pattern in a string.

    Parameters
    ----------
    pattern : str
        The regex pattern to search for.
    string : str
        The string to search in.

    Returns
    -------
    str or None
        The match object if the pattern is found, original string otherwise.

    Raises
    ------
    TypeError
        If pattern or string is not a string.
    """
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a string")
    if not isinstance(string, str):
        raise TypeError("string must be a string")

    match = re.search(pattern, string)
    return match.group(0) if match else None