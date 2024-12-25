from typing import Callable, Any, Optional
import warnings
import logging

def deprecated(logger: Optional[logging.Logger] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator to mark functions as deprecated. It will result in a warning being emitted when the function is used.

    Parameters
    ----------
    logger : Optional[logging.Logger]
        The logger to use for logging the deprecation warning. If None, the default logger will be used.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        A decorator that wraps the input function with deprecation warning logic.

    Raises
    ------
    TypeError
        If the logger is not an instance of logging.Logger or None.
    """
    if not isinstance(logger, logging.Logger) and logger is not None:
        raise TypeError("logger must be an instance of logging.Logger or None")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Decorator function to wrap the input function.

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
            Wrapper function to emit a deprecation warning and log a message.

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
            # Log the deprecation warning
            if logger is not None:
                logger.warning(f"Call to deprecated function {func.__name__}.", exc_info=True)
            # Emit a deprecation warning
            else:
                warnings.warn(f"{func.__name__} is deprecated.", DeprecationWarning, stacklevel=2)
            # Call the original function and return its result
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator