from typing import Callable, Any

def log_method_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        return func(self, *args, **kwargs)
    return wrapper
