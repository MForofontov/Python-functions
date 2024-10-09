from typing import List, Set

def add_strings_to_subsets(my_list: List[Set[str]], my_strings: List[str]) -> bool:
    """
    Clustering algorithm that finds a string in a list of strings in
    a list of sets and adds the whole list to the set if any string of 
    that list is inside the set.

    Parameters
    ----------
    my_list : list of sets
        The list of sets to add strings to.
    my_strings : list of str
        The list of strings to add to the sets.

    Returns
    -------
    bool
        True if any string was added to a set, False otherwise.
    """
    found = False
    for my_string in my_strings:
        if found:
            break
        for sublist in my_list:
            if my_string in sublist:
                sublist.update(my_strings)
                found = True
                break
    return found