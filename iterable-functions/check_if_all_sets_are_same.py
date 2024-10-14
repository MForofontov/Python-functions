from typing import List, Set, Any

def check_if_all_sets_are_same(sets_list: List[Set[Any]]) -> bool:
    """
    Checks if all sets within a list are identical.

    Parameters
    ----------
    sets_list : list
        A list of sets to be checked for identity.

    Returns
    -------
    bool
        True if all sets in the list are identical, False otherwise.
    """
    if len(sets_list) <= 1:
        return True
    
    reference_set = sets_list[0]
    
    for s in sets_list[1:]:
        if s != reference_set:
            return False
    
    return True