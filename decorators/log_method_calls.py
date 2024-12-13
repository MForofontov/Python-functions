from typing import Callable, Any

def log_method_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log method calls, including the arguments passed.

    Parameters
    ----------
    func : Callable[..., Any]
        The method to be decorated.

    Returns
    -------
    Callable[..., Any]
        The decorated method with logging.

    Raises
    ------
    None
    """
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """
        The wrapper function that logs the method calls.

        Parameters
        ----------
        self : Any
            The instance the method is called on.
        *args : Any
            Positional arguments for the decorated method.
        **kwargs : Any
            Keyword arguments for the decorated method.

        Returns
        -------
        Any
            The result of the decorated method.
        """
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper
