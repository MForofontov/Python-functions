from typing import List, Any, Union

def find_sublist_index(input_list_of_lists: List[List[Any]], target_value: Any) -> Union[int, None]:
    """
    Finds the index of the sublist that contains the target value within a list of lists.

    Parameters
    ----------
    input_list_of_lists : list of list
        The list of lists to search.
    target_value : any
        The value to find.

    Returns
    -------
    int or None
        The index of the sublist containing the element, or None if the string is not found in any sublist.
    """
    try:
        return input_list_of_lists.index(target_value)
    except ValueError:
        return None