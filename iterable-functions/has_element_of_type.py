from typing import List, Any

def has_element_of_type(input_list: List[Any], target_type: type) -> bool:
    """
    Check if any element in the input list matches the specified target type.

    Parameters
    ----------
    input_list : list
        The list to check for the presence of the target type.
    target_type : type
        The type to search for within the input list.

    Returns
    -------
    bool
        True if the target type is found in the input list, False otherwise.
    """
    for element in input_list:
        if isinstance(element, target_type):
            return True
    return False