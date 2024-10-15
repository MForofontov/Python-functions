from typing import Callable, TypeVar
import asyncio

# Define a type variable T to represent the return type of the task
T = TypeVar('T')

async def async_cancellable_task(task: Callable[[], T], cancel_event: asyncio.Event) -> T:
    """
    Run an asynchronous task that can be cancelled.

    Parameters
    ----------
    task : Callable[[], T]
        The asynchronous function to run.
    cancel_event : asyncio.Event
        The event used to signal cancellation.

    Returns
    -------
    T
        The result of the task if completed before cancellation.

    Raises
    ------
    asyncio.CancelledError
        If the task is cancelled.

    Examples
    --------
    >>> async def long_running_task() -> str:
    >>>     await asyncio.sleep(10)
    >>>     return "Completed"
    >>> 
    >>> cancel_event = asyncio.Event()
    >>> result = asyncio.run(async_cancellable_task(long_running_task, cancel_event))
    """
    try:
        # Attempt to run the task with a timeout of 5 seconds
        result = await asyncio.wait_for(task(), timeout=5)
        return result
    except asyncio.TimeoutError:
        # If a timeout occurs, set the cancel event and raise a CancelledError
        cancel_event.set()
        raise asyncio.CancelledError("Task was cancelled.")