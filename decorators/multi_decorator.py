from typing import Callable, Any

def multi_decorator(*decorators: Callable[[Callable[..., Any]], Callable[..., Any]]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A higher-order decorator to apply multiple decorators to a single function.

    Parameters
    ----------
    *decorators : Callable[[Callable[..., Any]], Callable[..., Any]]
        A variable number of decorators to apply.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        A function that applies all the decorators to the target function.
    """
    def combine(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        The function that applies all the decorators to the target function.

        Parameters
        ----------
        func : Callable[..., Any]
            The function to be decorated.

        Returns
        -------
        Callable[..., Any]]
            The decorated function.
        """
        for decorator in reversed(decorators):
            func = decorator(func)
        return func
    return combine
