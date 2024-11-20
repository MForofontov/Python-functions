import itertools
from typing import Any, List

def flatten_list(list_to_flatten: List[List[Any]]) -> List[Any]:
    """
    Flatten one level of a nested list.

    Parameters
    ----------
    list_to_flatten : list
        Nested list to flatten.

    Returns
    -------
    list
        Input list flattened by one level.

    Raises
    ------
    TypeError
        If list_to_flatten is not a list of lists.
    """
    if not isinstance(list_to_flatten, list) or not all(isinstance(sublist, list) for sublist in list_to_flatten):
        raise TypeError("list_to_flatten must be a list of lists")

    return list(itertools.chain(*list_to_flatten))
