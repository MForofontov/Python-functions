from typing import Callable, Any

def manipulate_output(manipulation_func: Callable[[str], str]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to manipulate the output of a function using a specified manipulation function.

    Parameters
    ----------
    manipulation_func : Callable[[str], str]
        The function to manipulate the output of the decorated function.

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
            The wrapper function that manipulates the output of the decorated function.

            Parameters
            ----------
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            str
                The manipulated output of the decorated function.
            """
            result = func(*args, **kwargs)
            return manipulation_func(result)
        return wrapper
    return decorator
