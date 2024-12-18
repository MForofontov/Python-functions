from typing import Callable, Any
import asyncio
import inspect
import logging

def async_handle_error(error_message: str, log_errors: bool = False) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator to handle errors in asynchronous functions.

    Parameters
    ----------
    error_message : str
        The error message to print when an exception occurs.
    log_errors : bool, optional
        Whether to log errors using the logging module. Default is False.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        A decorator that wraps the input function with error handling.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Decorator function.

        Parameters
        ----------
        func : Callable[..., Any]
            The asynchronous function to be wrapped.

        Returns
        -------
        Callable[..., Any]
            The wrapped function with error handling.

        Raises
        ------
        TypeError
            If the function is not asynchronous.
        """
        if not inspect.iscoroutinefunction(func):
            error_message = "The function to be wrapped must be asynchronous"
            if log_errors:
                logging.error(error_message)
            raise TypeError("The function to be decorated must be asynchronous")

        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapper function to handle errors in the asynchronous function.

            Parameters
            ----------
            *args : Any
                Positional arguments to pass to the wrapped function.
            **kwargs : Any
                Keyword arguments to pass to the wrapped function.

            Returns
            -------
            Any
                The result of the wrapped function, or None if an exception occurs.
            """
            try:
                # Attempt to call the original asynchronous function
                return await func(*args, **kwargs)
            except Exception as e:
                # Print the custom error message and the exception
                print(f"{error_message}: {e}")
                # Log the error message and the exception if logging is enabled
                if log_errors:
                    logging.error(f"{error_message}: {e}")
                # Return None if an exception occurs
                return None
        return wrapper
    return decorator
