from typing import List

def repeat_strings_in_a_list(string: str, times: int) -> List[str]:
    """
    Creates a list where a given character is repeated a specified number of times.

    Parameters
    ----------
    string : str
        The character to be repeated.
    times : int
        The number of times the character should be repeated.

    Returns
    -------
    list of str
        A list containing the character repeated 'times' times.
    """
    return [string for _ in range(times)]