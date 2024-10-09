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
    """
    return list(itertools.chain(*list_to_flatten))