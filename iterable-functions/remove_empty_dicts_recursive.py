from typing import Dict, Any

def remove_empty_dicts_recursive(nested_dict: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Recursively removes empty dictionary entries from a nested dictionary.

    Parameters
    ----------
    nested_dict : dict
        The nested dictionary.

    Returns
    -------
    dict
        The nested dictionary with empty dictionaries removed.
    """
    if isinstance(nested_dict, dict):
        for key in list(nested_dict.keys()):
            nested_dict[key] = remove_empty_dicts_recursive(nested_dict[key])
            if not nested_dict[key] and not isinstance(nested_dict[key], (bool, int, float)):
                del nested_dict[key]
    return nested_dict