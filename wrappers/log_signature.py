from typing import Callable, Any
import inspect

def log_signature(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        signature = inspect.signature(func)
        print(f"Executing {func.__name__}{signature} with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
