from multiprocessing import Pool, cpu_count
from typing import Callable, List, TypeVar, Tuple

# Define type variables for input and output types
T = TypeVar('T')
R = TypeVar('R')

def parallel_gather_errors(func: Callable[[T], R], data: List[T], num_processes: int = None) -> Tuple[List[R], List[Exception]]:
    """
    Apply a function to a list of items in parallel and gather any exceptions raised by the processes.

    Parameters
    ----------
    func : Callable[[T], R]
        The function to apply to each item in the list.
    data : List[T]
        The list of data items to process.
    num_processes : int, optional
        The number of processes to use for parallel execution. If None, it defaults 
        to the number of available CPUs (by default None).

    Returns
    -------
    Tuple[List[R], List[Exception]]
        A tuple containing the list of results and the list of exceptions. If an exception occurs 
        for an item, its corresponding result is not included in the result list.

    Examples
    --------
    >>> def risky_func(x: int) -> int:
    >>>     if x == 2:
    >>>         raise ValueError("Bad value!")
    >>>     return x * x
    >>> parallel_gather_errors(risky_func, [1, 2, 3])
    ([1, 9], [ValueError('Bad value!')])
    """
    # Initialize lists to store results and errors
    results = []
    errors = []

    def wrapper(item):
        """
        Wrapper function to apply the given function and catch exceptions.

        Parameters
        ----------
        item : T
            The data item to process.

        Returns
        -------
        Tuple[Optional[R], Optional[Exception]]
            A tuple containing the result or the exception if an error occurred.
        """
        try:
            return func(item), None
        except Exception as e:
            return None, e

    # If num_processes is not specified, default to the number of available CPUs minus one
    if num_processes is None:
        num_processes = cpu_count() - 1  # Pool will default to the number of available CPUs (minus 1)

    # Create a pool of worker processes
    with Pool(processes=num_processes) as pool:
        # Apply the wrapper function to each item in the data list in parallel
        processed = pool.map(wrapper, data)
    
    # Separate results and errors
    for result, error in processed:
        if error:
            errors.append(error)
        else:
            results.append(result)
    
    # Return the list of results and the list of errors
    return results, errors
