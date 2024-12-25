from typing import Callable, Any, Dict, List

class EventManager:
    """
    A class to manage events and their associated callbacks.

    Attributes
    ----------
    events : Dict[str, List[Callable[..., Any]]]
        A dictionary where the keys are event names and the values are lists of callback functions.

    Methods
    -------
    __init__():
        Initializes the EventManager with an empty events dictionary.
    subscribe(event_name: str, callback: Callable[..., Any]):
        Adds a callback function to the list of callbacks for a given event name.
    trigger(event_name: str, *args: Any, **kwargs: Any):
        Executes all callback functions associated with the given event name.
    """
    def __init__(self):
        """
        Initializes the EventManager with an empty events dictionary.
        """
        self.events: Dict[str, List[Callable[..., Any]]] = {}

    def subscribe(self, event_name: str, callback: Callable[..., Any]):
        """
        Adds a callback function to the list of callbacks for a given event name.

        Parameters
        ----------
        event_name : str
            The name of the event.
        callback : Callable[..., Any]
            The callback function to be added.
        """
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(callback)

    def trigger(self, event_name: str, *args: Any, **kwargs: Any):
        """
        Executes all callback functions associated with the given event name.

        Parameters
        ----------
        event_name : str
            The name of the event.
        *args : Any
            Positional arguments to pass to the callback functions.
        **kwargs : Any
            Keyword arguments to pass to the callback functions.
        """
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args, **kwargs)

def event_trigger(event_name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to trigger an event before executing the decorated function.

    Parameters
    ----------
    event_name : str
        The name of the event to trigger.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        The actual decorator function.

        Parameters
        ----------
        func : Callable[..., Any]
            The function to be decorated.

        Returns
        -------
        Callable[..., Any]
            The wrapped function.
        """
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            The wrapper function that triggers the event and then calls the original function.

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
            """
            EventManager().trigger(event_name, *args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator


