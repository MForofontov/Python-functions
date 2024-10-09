from typing import Any, Set

def convert_set_elements_to_strings(input_set: Set[Any]) -> Set[str]:
    """
    Convert all elements in the set to strings.

    Parameters
    ----------
    input_set : set
        The set of elements to be converted to strings.

    Returns
    -------
    set
        A set with all elements converted to strings.
    """
    return {str(element) for element in input_set}