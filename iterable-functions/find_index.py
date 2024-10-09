from typing import List, Union

def find_index(input_list: List[str], target_string: str) -> Union[int, None]:
    """
    Find the index of a string in a list.

    Parameters
    ----------
    input_list : list
        The list to search.
    target_string : str
        The string to find.

    Returns
    -------
    int or None
        The index of the string in the list, or None if the string is not found.
    """
    try:
        return input_list.index(target_string)
    except ValueError:
        return None