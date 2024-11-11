from typing import Dict, Any

def identify_string_in_dict_get_value(search_key: str, search_dict: Dict[str, Any]) -> Any:
    """
    Identify the value in the dictionary where the search key is present.

    Parameters
    ----------
    search_key : str
        The key to find.
    search_dict : dict
        The dictionary where to find the key.

    Returns
    -------
    Any
        The value of the entry where the key is present, or None if not found.
    """
    for key, value in search_dict.items():
        if search_key in value:
            return value
    return None