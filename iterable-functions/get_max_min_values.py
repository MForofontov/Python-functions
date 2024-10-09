from typing import List, Any, Union, Tuple

def get_max_min_values(input_list: List[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    """
    From an input list, return the maximum and minimum integer or float values.

    Parameters
    ----------
    input_list : list[int] or list[float]
        List containing integer or float values.

    Returns
    -------
    tuple
        A tuple containing the largest and smallest values in the input list.
    """
    return max(input_list), min(input_list)