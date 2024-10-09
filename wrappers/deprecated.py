from typing import Callable, Any
import warnings

def deprecated(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to mark functions as deprecated. It will result in a warning being emitted when the function is used.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be marked as deprecated.

    Returns
    -------
    Callable[..., Any]
        A wrapper function that emits a deprecation warning when the input function is called.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to emit a deprecation warning.

        Parameters
        ----------
        *args : Any
            Positional arguments to pass to the wrapped function.
        **kwargs : Any
            Keyword arguments to pass to the wrapped function.

        Returns
        -------
        Any
            The result of the wrapped function.
        """
        warnings.warn(f"{func.__name__} is deprecated.", DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper