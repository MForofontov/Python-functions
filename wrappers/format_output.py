from typing import Callable, Any

def format_output(format_string: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)
            return format_string.format(result)
        return wrapper
    return decorator
