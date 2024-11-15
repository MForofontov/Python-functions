from typing import Dict, List, Any
from collections import Counter

def get_shared_elements(dict_: Dict[str, List[Any]]) -> List[Any]:
    """
    Identify elements that appear in at least two lists within a dictionary.

    Parameters
    ----------
    dict_ : dict
        A dictionary where the values are lists of elements.

    Returns
    -------
    list
        A list containing elements that appear in at least two lists within the dictionary.

    Raises
    ------
    TypeError
        If dict_ is not a dictionary or if any value in dict_ is not a list.
    """
    if not isinstance(dict_, dict):
        raise TypeError("dict_ must be a dictionary")
    if not all(isinstance(value, list) for value in dict_.values()):
        raise TypeError("All values in dict_ must be lists")

    all_elements = [elem for sublist in dict_.values() for elem in sublist]
    element_counts = Counter(all_elements)
    shared_elements = [elem for elem, count in element_counts.items() if count >= 2]
    return shared_elements