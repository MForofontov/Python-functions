from typing import Callable, Any
import time

def rate_limit(max_calls: int, period: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to limit the number of times a function can be called within a specific period.

    Parameters
    ----------
    max_calls : int
        The maximum number of allowed calls within the period.
    period : int
        The time period in seconds.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        # List to store the timestamps of function calls
        calls = []

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            The wrapper function that enforces the rate limit.

            Parameters
            ----------
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            Any
                The result of the decorated function.

            Raises
            ------
            Exception
                If the rate limit is exceeded.
            """
            nonlocal calls  # Indicates that 'calls' refers to the list in the enclosing scope
            current_time = time.time()
            # Filter out calls that are outside the period
            calls = [call for call in calls if current_time - call < period]

            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded. Try again later.")

            # Append the current timestamp to the list of calls
            calls.append(current_time)
            return func(*args, **kwargs)

        return wrapper
    return decorator
