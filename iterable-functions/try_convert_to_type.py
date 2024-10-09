from typing import Any

def try_convert_to_type(value: Any, target_type: type) -> Any:
    """
    Attempts to convert a given value to a specified type.

    Parameters
    ----------
    value : Any
        The value to be converted.
    target_type : type
        The type to which `value` should be converted.

    Returns
    -------
    Any
        The converted value if the conversion is successful; otherwise, the original value.
    """
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return value