from typing import Callable, Any, TypeVar, Optional

T = TypeVar('T')

def conditional_execute(predicate: Callable[[], bool]) -> Callable[[Callable[..., T]], Callable[..., Optional[T]]]:
    """
    Decorator to conditionally execute a function based on a predicate.

    Parameters
    ----------
    predicate : Callable[[], bool]
        A function that returns a boolean value. The decorated function will only be executed if this predicate returns True.

    Returns
    -------
    Callable[[Callable[..., T]], Callable[..., Optional[T]]]
        A decorator that wraps the input function with conditional execution logic.
    """
    if not callable(predicate):
        raise TypeError("Predicate must be callable")

    def decorator(func: Callable[..., T]) -> Callable[..., Optional[T]]:
        """
        Decorator function.

        Parameters
        ----------
        func : Callable[..., T]
            The function to be conditionally executed.

        Returns
        -------
        Callable[..., Optional[T]]
            The wrapped function with conditional execution logic.
        """
        def wrapper(*args: Any, **kwargs: Any) -> Optional[T]:
            """
            Wrapper function to conditionally execute the input function.

            Parameters
            ----------
            *args : Any
                Positional arguments to pass to the wrapped function.
            **kwargs : Any
                Keyword arguments to pass to the wrapped function.

            Returns
            -------
            Optional[T]
                The result of the wrapped function if the predicate returns True, otherwise None.
            """
            if predicate():
                return func(*args, **kwargs)
            return None
        
        return wrapper
    
    return decorator