from typing import Callable, Any
from contextlib import contextmanager

def context_manager(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to convert a function into a context manager.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be converted into a context manager.

    Returns
    -------
    Callable[..., Any]
        A wrapper function that provides context management for the input function.
    """
    @contextmanager
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to provide context management.

        Parameters
        ----------
        *args : Any
            Positional arguments to pass to the wrapped function.
        **kwargs : Any
            Keyword arguments to pass to the wrapped function.

        Yields
        ------
        Any
            The result of the wrapped function.

        Ensures
        -------
        The cleanup code is executed after the context is exited.
        """
        try:
            result = func(*args, **kwargs)
            yield result
        finally:
            print(f"{func.__name__} has been cleaned up.")
    return wrapper