from typing import Any, Dict, Tuple
from collections import OrderedDict

def sort_subdict_by_tuple(dict_: Dict[str, Dict[str, Any]], order: Tuple[str, ...]) -> Dict[str, OrderedDict]:
    """
    Sorts the sub-dictionaries of a given dictionary based on a specified order tuple.

    Parameters
    ----------
    dict_ : Dict[str, Dict[str, Any]]
        The input dictionary containing sub-dictionaries as values.
    order : Tuple[str, ...]
        A tuple specifying the desired order of keys in the sorted sub-dictionaries.

    Returns
    -------
    Dict[str, OrderedDict]
        A new dictionary with each sub-dictionary sorted according to the specified order.

    Raises
    ------
    TypeError
        If dict_ is not a dictionary of dictionaries or order is not a tuple of strings.
    """
    if not isinstance(dict_, dict) or not all(isinstance(subdict, dict) for subdict in dict_.values()):
        raise TypeError("dict_ must be a dictionary with sub-dictionaries as values")
    if not isinstance(order, tuple) or not all(isinstance(item, str) for item in order):
        raise TypeError("order must be a tuple of strings")

    sorted_data: Dict[str, OrderedDict] = {}
    for key, subdict in dict_.items():
        sorted_subdict = OrderedDict(
            sorted(subdict.items(), key=lambda item: order.index(item[0]) if item[0] in order else len(order))
        )
        sorted_data[key] = sorted_subdict
    return sorted_data