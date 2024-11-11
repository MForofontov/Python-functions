from typing import Any, List

def isListEmpty(input_list: List[Any]) -> bool:
    """
    Check if a nested list is empty.
    
    Parameters
    ----------
    input_list : list
        Input list to verify

    Returns
    -------
    bool
        If list is empty or not.
    """
    if isinstance(input_list, list):
        return all(map(isListEmpty, input_list)) if isinstance(input_list, list) else False