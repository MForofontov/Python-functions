from typing import Callable, Any
from contextlib import redirect_stdout

def redirect_output(file_path: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to redirect the standard output of a function to a specified file.

    Parameters
    ----------
    file_path : str
        The path to the file where the output should be redirected.

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
            The wrapper function that redirects the output.

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
            # Open the specified file in write mode
            with open(file_path, 'w') as f:
                # Redirect stdout to the file
                with redirect_stdout(f):
                    # Call the original function and return its result
                    return func(*args, **kwargs)
        return wrapper
    return decorator
