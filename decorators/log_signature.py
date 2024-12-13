from typing import Callable, Any
import inspect

def log_signature(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log the function signature and the arguments passed to it.

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
        The wrapper function that logs the function signature and arguments.

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
        signature = inspect.signature(func)
        print(f"Executing {func.__name__}{signature} with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
