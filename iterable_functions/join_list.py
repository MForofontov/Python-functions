from typing import List

def join_list(lst: List[str], delimiter: str) -> str:
    """
    Join all elements in a list into a single string.

    Parameters
    ----------
    lst : list
        List with elements to be joined.
    delimiter : str
        Character used to join list elements.

    Returns
    -------
    str
        A single string with all elements in the input list joined by the character chosen as link.
    """
    return delimiter.join(lst)