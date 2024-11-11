from typing import List, Any

def get_unique_sublists(list_of_lists: List[List[Any]]) -> List[List[Any]]:
    """
    Identify unique sublists within a list of lists.

    Parameters
    ----------
    list_of_lists : list
        The list containing various sublists.

    Returns
    -------
    list
        List containing unique sublists.
    """
    seen = set()
    unique_sublists = []
    for sublist in list_of_lists:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            unique_sublists.append(sublist)
    return unique_sublists