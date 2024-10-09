from typing import List
import re

def regex_present(regex_list: List[str], string: str) -> bool:
    """
    Check if any regex in a list is found in a string.

    Parameters
    ----------
    regex_list : list of str
        The list of regexes to search for in the string.
    string : str
        The string to search in.

    Returns
    -------
    bool
        True if any regex is found in the string, False otherwise.
    """
    return any(re.search(regex, string) for regex in regex_list)