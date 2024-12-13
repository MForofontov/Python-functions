from typing import Callable, Any

def chain(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to call the 'chain' method on the result of a function if it exists.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be wrapped.

    Returns
    -------
    Callable[..., Any]
        A wrapper function that calls the 'chain' method on the result of the input function if it exists.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to call the 'chain' method on the result of the input function if it exists.

        Parameters
        ----------
        *args : Any
            Positional arguments to pass to the wrapped function.
        **kwargs : Any
            Keyword arguments to pass to the wrapped function.

        Returns
        -------
        Any
            The result of the wrapped function, or the result of calling its 'chain' method if it exists.
        """
        result = func(*args, **kwargs)
        if hasattr(result, 'chain'):
            return result.chain()
        return result
    
    return wrapper