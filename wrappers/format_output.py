from typing import Callable, Any

def format_output(format_string: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to format the output of a function according to a specified format string.

    Parameters
    ----------
    format_string : str
        The format string to use for formatting the output.

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
        def wrapper(*args: Any, **kwargs: Any) -> str:
            """
            The wrapper function that formats the output of the decorated function.

            Parameters
            ----------
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            str
                The formatted output of the decorated function.
            """
            result = func(*args, **kwargs)
            return format_string.format(result)
        return wrapper
    return decorator