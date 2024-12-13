from typing import Callable, Any, Dict, Tuple
import time

def memoize_with_expiration(expiration_time: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to cache the results of a function call for a specified amount of time.

    Parameters
    ----------
    expiration_time : int
        The time in seconds for which the cached result is valid.

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
        cache: Dict[Tuple, Tuple[float, Any]] = {}

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
            current_time = time.time()
            if key in cache:
                cached_time, cached_value = cache[key]
                if current_time - cached_time < expiration_time:
                    return cached_value
            result = func(*args, **kwargs)
            cache[key] = (current_time, result)
            return result

        return wrapper
    return decorator
