from typing import Callable, Any

def normalize_input(normalization_func: Callable[[Any], Any]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to normalize the input arguments of a function.

    Parameters
    ----------
    normalization_func : Callable[[Any], Any]
        The function to normalize each input argument.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.
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
            The wrapper function that normalizes the input arguments.

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
            normalized_args = [normalization_func(arg) for arg in args]
            return func(*normalized_args, **kwargs)
        return wrapper
    return decorator
