from multiprocessing import Pool, cpu_count
from typing import Callable, List, TypeVar

# Define a type variable for the input type
T = TypeVar('T')

def parallel_filter(condition: Callable[[T], bool], data: List[T], num_processes: int = None) -> List[T]:
    """
    Filter a list of items in parallel, keeping only those that satisfy the condition.

    Parameters
    ----------
    condition : Callable[[T], bool]
        A function that takes an item as input and returns `True` if the item should be kept, `False` otherwise.
    data : List[T]
        The list of data items to filter.
    num_processes : int, optional
        The number of processes to use for parallel execution. If None, it defaults 
        to the number of available CPUs (by default None).

    Returns
    -------
    List[T]
        A list containing only the items that satisfy the condition.

    Examples
    --------
    >>> def is_even(x: int) -> bool:
    >>>     return x % 2 == 0
    >>> parallel_filter(is_even, [1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    # If num_processes is not specified, use the number of available CPUs
    if num_processes is None:
        num_processes = cpu_count - 1  # Pool will default to the number of available CPUs (minus 1)
    
    # Create a pool of worker processes
    with Pool(processes=num_processes) as pool:
        # Apply the condition function to the data in parallel
        results = pool.map(condition, data)
    
    # Return a list of items that satisfy the condition
    return [item for item, keep in zip(data, results) if keep]