from typing import Callable, Any, Dict, List

class EventManager:
    def __init__(self):
        self.events: Dict[str, List[Callable[..., Any]]] = {}

    def subscribe(self, event_name: str, callback: Callable[..., Any]):
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(callback)

    def trigger(self, event_name: str, *args: Any, **kwargs: Any):
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args, **kwargs)

def event_trigger(event_name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            event_manager.trigger(event_name, *args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Initialize EventManager
event_manager = EventManager()
