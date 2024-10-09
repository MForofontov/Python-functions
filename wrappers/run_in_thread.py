from typing import Callable, Any
from threading import Thread

def run_in_thread(func: Callable[..., Any]) -> Callable[..., None]:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper