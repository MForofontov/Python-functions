from typing import List, Any

def check_if_all_elements_are_duplicates(input_list: List[Any]) -> bool:
    """
    Check if all elements in the list are duplicates.

    Parameters
    ----------
    input_list : list
        The list to check for duplicate elements.

    Returns
    -------
    bool
        True if every element in the list occurs more than once, False otherwise.
        Returns False if the list is empty.

    Raises
    ------
    TypeError
        If input_list is not a list.
    """
    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list")

    element_counts = {}
    for element in input_list:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    
    for count in element_counts.values():
        if count == 1:
            return False
    return True if element_counts else False