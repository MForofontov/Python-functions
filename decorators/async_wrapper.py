from typing import Callable, Any
import asyncio

def async_wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Wraps a synchronous function to be executed asynchronously.

    Parameters
    ----------
    func : Callable[..., Any]
        The synchronous function to be wrapped.

    Returns
    -------
    Callable[..., Any]
        An asynchronous wrapper function that executes the input function in an executor.
    """
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
        # Get the current event loop
        loop = asyncio.get_event_loop()
        # Run the synchronous function in an executor and return the result
        return await loop.run_in_executor(None, func, *args, **kwargs)
    
    return wrapper