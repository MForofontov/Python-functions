from typing import Callable, Any
import asyncio
import logging
import inspect

def async_wrapper(func: Callable[..., Any], log_errors: bool = False) -> Callable[..., Any]:
    """
    Wraps a synchronous function to be executed asynchronously.

    Parameters
    ----------
    func : Callable[..., Any]
        The synchronous function to be wrapped.
    log_errors : bool, optional
        Whether to log errors using the logging module. Default is False.

    Returns
    -------
    Callable[..., Any]
        An asynchronous wrapper function that executes the input function in an executor.

    Raises
    ------
    TypeError
        If the function is not synchronous.
    """
    if inspect.iscoroutinefunction(func):
        error_message = "The function to be wrapped must be synchronous"
        if log_errors:
            logging.error(f"An error occurred in {func.__name__}: {error_message}")
        raise TypeError(error_message)

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Asynchronous wrapper function.

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
        try:
            # Get the current event loop
            loop = asyncio.get_event_loop()
            # Run the synchronous function in an executor and return the result
            return await loop.run_in_executor(None, func, *args, **kwargs)
        except Exception as e:
            if log_errors:
                logging.error(f"An error occurred in {func.__name__}: {e}", exc_info=True)
            raise

    return wrapper
