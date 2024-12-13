from typing import Callable, Any

def handle_error(error_message: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to handle exceptions in the decorated function. If an exception occurs,
    it prints a specified error message and returns None.

    Parameters
    ----------
    error_message : str
        The error message to print if an exception occurs.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.

    Raises
    ------
    None
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        The actual decorator function.

        Parameters
        ----------
        func : Callable[..., Any]
            The function to be decorated.

        Returns
        -------
        Callable[..., Any]
            The wrapped function.
        """
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            The wrapper function that handles exceptions.

            Parameters
            ----------
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            Any
                The result of the decorated function, or None if an exception occurs.
            """
            try:
                return func(*args, **kwargs)
            except Exception:
                print(error_message)
                return None
        return wrapper
    return decorator
