from typing import Any, Dict, Tuple
from collections import OrderedDict

def sort_subdict_by_tuple(dict_: Dict[str, Dict[str, Any]], order: Tuple[str, ...]) -> Dict[str, OrderedDict]:
    """
    Sorts the sub-dictionaries of a given dictionary based on a specified order tuple.

    Parameters
    ----------
    dict_ : dict
        The input dictionary containing sub-dictionaries as values.
    order : tuple
        A tuple specifying the desired order of keys in the sorted sub-dictionaries.

    Returns
    -------
    dict
        A new dictionary with each sub-dictionary sorted according to the specified order.
    """
    sorted_data = {}
    for key, subdict in dict_.items():
        sorted_subdict = OrderedDict(sorted(subdict.items(), key=lambda item: order.index(item[0]) if item[0] in order else len(order)))
        sorted_data[key] = sorted_subdict
    return sorted_data