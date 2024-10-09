from typing import Callable, Any

def manipulate_output(manipulation_func: Callable[[str], str]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)
            return manipulation_func(result)
        return wrapper
    return decorator
