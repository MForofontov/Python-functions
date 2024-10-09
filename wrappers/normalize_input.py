from typing import Callable, Any

def normalize_input(normalization_func: Callable[[Any], Any]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            normalized_args = [normalization_func(arg) for arg in args]
            return func(*normalized_args, **kwargs)
        return wrapper
    return decorator
