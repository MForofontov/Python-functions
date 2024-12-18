from typing import Callable, Any, Dict, Tuple, FrozenSet

def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to cache the results of a function call.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be cached.

    Returns
    -------
    Callable[..., Any]
        A wrapper function that caches the results of the input function.
    """
    cached_results: Dict[Tuple[Tuple[Any, ...], FrozenSet[Tuple[str, Any]]], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to cache the results of the input function.

        Parameters
        ----------
        *args : Any
            Positional arguments to pass to the wrapped function.
        **kwargs : Any
            Keyword arguments to pass to the wrapped function.

        Returns
        -------
        Any
            The cached result of the wrapped function.
        """
        key = (args, frozenset(kwargs.items()))
        if key not in cached_results:
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]
    
    return wrapper