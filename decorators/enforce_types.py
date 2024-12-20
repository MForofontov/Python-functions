import logging
from typing import Callable, Any, get_type_hints, Optional

def enforce_types(func: Callable[..., Any], logger: Optional[logging.Logger] = None) -> Callable[..., Any]:
    """
    A decorator to enforce type hints on the arguments of a function.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be decorated.
    logger : Optional[logging.Logger]
        The logger to use for logging errors. If None, the default logger is used.

    Returns
    -------
    Callable[..., Any]
        The decorated function with type enforcement.

    Raises
    ------
    TypeError
        If an argument does not match the expected type.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        The wrapper function that checks the types of the arguments.

        Parameters
        ----------
        *args : Any
            Positional arguments for the decorated function.
        **kwargs : Any
            Keyword arguments for the decorated function.

        Returns
        -------
        Any
            The result of the decorated function.

        Raises
        ------
        TypeError
            If an argument does not match the expected type.
        """
        hints = get_type_hints(func)
        for arg_name, arg_value in zip(hints.keys(), args):
            expected_type = hints[arg_name]
            if not isinstance(arg_value, expected_type):
                error_message = f"Expected {expected_type} for argument '{arg_name}', got {type(arg_value)}."
                if logger:
                    logger.error(error_message, exc_info=True)
                else:
                    raise TypeError(error_message)
        for arg_name, arg_value in kwargs.items():
            if arg_name in hints:
                expected_type = hints[arg_name]
                if not isinstance(arg_value, expected_type):
                    error_message = f"Expected {expected_type} for argument '{arg_name}', got {type(arg_value)}."
                    if logger:
                        logger.error(error_message, exc_info=True)
                    else:
                        raise TypeError(error_message)
        return func(*args, **kwargs)

    return wrapper
    