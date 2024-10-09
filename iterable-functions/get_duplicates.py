from collections import Counter
from typing import List, Any

def get_duplicates(input_list: List[Any]) -> List[Any]:
    """
    Identify duplicate elements in a list.

    Parameters
    ----------
    input_list : list
        The list to check for duplicate elements.

    Returns
    -------
    list
        A list containing the duplicate elements found in the input list.
    """
    element_counts = Counter(input_list)
    duplicates = [element for element, count in element_counts.items() if count > 1]
    return duplicates