from typing import List, Any

def all_match_lists(list1: List[Any], list2: List[Any]) -> bool:
    """
    Check if all elements of list1 are contained in list2.

    Parameters
    ----------
    list1 : list
        The query list to check for full containment.
    list2 : list
        The subject list to compare against the query list.

    Returns
    -------
    bool
        True if all elements of list1 are found in list2, False otherwise.
    """
    return all(elem in list2 for elem in list1)