import logging
from typing import Callable, Any

def log_function_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log the function calls, including the arguments passed and the result returned.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be decorated.

    Returns
    -------
    Callable[..., Any]
        The decorated function with logging.

    Raises
    ------
    None
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        The wrapper function that logs the function calls.

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
        """
        logging.info(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper
