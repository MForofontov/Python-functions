from typing import Any, List

def partially_contains_fragment_of_list(target_list: List[Any], list_of_lists: List[List[Any]]) -> bool:
    """
    Check if the target_list is contained inside sublist even if it partially.
    e.g partially_contains_fragment_of_list(['a', 'b'], [['a', 'b', 'c'], ['d', 'e']])
    returns True.
    
    Parameters
    ----------
    target_list : list
        List to find inside the list_of_lists.
    list_of_lists : list
        The nested list.

    Returns
    -------
    bool
        True if contains False if not.
    """
    for sub in list_of_lists:
        if any(sub[i:i+len(target_list)] == target_list for i in range(len(sub)-len(target_list)+1)):
            return True
    return False