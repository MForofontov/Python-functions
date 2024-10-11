import os
from typing import Callable, Any

def env_config(var_name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to check for an environment variable before executing the function.

    Parameters
    ----------
    var_name : str
        The name of the environment variable to check.

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
            The wrapper function that checks the environment variable.

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
            if var_name in os.environ:
                print(f"Using environment variable {var_name} with value: {os.environ[var_name]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator