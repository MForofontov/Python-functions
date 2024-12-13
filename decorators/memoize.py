from typing import Callable, Any, Dict, Tuple

def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to cache the results of a function call.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be decorated.

    Returns
    -------
    Callable[..., Any]
        The decorated function with caching.
    """
    cache: Dict[Tuple, Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        The wrapper function that caches the result of the decorated function.

        Parameters
        ----------
        *args : Any
            Positional arguments for the decorated function.
        **kwargs : Any
            Keyword arguments for the decorated function.

        Returns
        -------
        Any
            The result of the decorated function, either from the cache or freshly computed.
        """
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper
