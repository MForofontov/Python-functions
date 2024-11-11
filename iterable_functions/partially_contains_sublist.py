from typing import List, Any
from any_match_lists import any_match_lists

def partially_contains_sublist(main_list: List[Any], list_of_lists: List[List[Any]]) -> bool:
    """
    Check if elements of the main list are partially contained in any sublist of the list of lists.

    Parameters
    ----------
    main_list : list
        The query list to check for partial containment.
    list_of_lists : list
        The subject list containing sublists to compare against the query list.

    Returns
    -------
    bool
        True if any element of the main list is partially contained in any sublist of the list of lists, False otherwise.
    """
    for sublist in list_of_lists:
        if any_match_lists(main_list, sublist):
            return True
    return False