import os
from typing import Callable, Any

def env_config(var_name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if var_name in os.environ:
                print(f"Using environment variable {var_name} with value: {os.environ[var_name]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
