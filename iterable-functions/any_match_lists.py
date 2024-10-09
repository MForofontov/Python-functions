from typing import List, Any

def any_match_lists(list1: List[Any], list2: List[Any]) -> bool:
    """
    Check if any element of list1 is contained in list2.

    Parameters
    ----------
    list1 : list
        The query list to check for partial containment.
    list2 : list
        The subject list to compare against the query list.

    Returns
    -------
    bool
        True if any element of list1 is found in list2, False otherwise.
    """
    return any(elem in list2 for elem in list1)