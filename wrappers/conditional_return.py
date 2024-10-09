from typing import Callable, Any

def conditional_return(condition: Callable[..., bool], return_value: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator to conditionally return a specified value based on a condition.

    Parameters
    ----------
    condition : Callable[..., bool]
        A function that returns a boolean value. The decorated function will return `return_value` if this condition returns True.
    return_value : Any
        The value to return if the condition is met.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        A decorator that wraps the input function with conditional return logic.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Decorator function.

        Parameters
        ----------
        func : Callable[..., Any]
            The function to be conditionally executed.

        Returns
        -------
        Callable[..., Any]
            The wrapped function with conditional return logic.
        """
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapper function to conditionally return a specified value.

            Parameters
            ----------
            *args : Any
                Positional arguments to pass to the wrapped function.
            **kwargs : Any
                Keyword arguments to pass to the wrapped function.

            Returns
            -------
            Any
                The specified return value if the condition is met, otherwise the result of the wrapped function.
            """
            if condition(*args, **kwargs):
                return return_value
            return func(*args, **kwargs)
        return wrapper
    return decorator