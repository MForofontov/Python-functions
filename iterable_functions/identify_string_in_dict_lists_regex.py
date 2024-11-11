from typing import Dict, List, Union
from remove_by_regex import remove_by_regex

def identify_string_in_dict_lists_regex(target_value: str, dict_of_lists: Dict[Union[str, int], List[List[str]]], regex: bool = False) -> Union[str, int, bool]:
    """
    Identifies if a string is present in any list inside a dictionary.

    Parameters
    ----------
    target_value : str
        The value to find.
    dict_of_lists : dict
        A dictionary where the values are lists of lists.
    regex : bool, optional
        A regex pattern to search for in the lists.

    Returns
    -------
    int or str or bool
        The key of the entry where the string is present, or False if not found.
    """
    for key, lists in dict_of_lists.items():
        for list_ in lists:
            if target_value in [remove_by_regex(l, regex) for l in list_] if regex else list_:
                return key
    return False