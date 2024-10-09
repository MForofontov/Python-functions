from typing import Callable, Any
import sys
from contextlib import redirect_stdout
from io import StringIO

def redirect_output(file_path: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with open(file_path, 'w') as f:
                with redirect_stdout(f):
                    return func(*args, **kwargs)
        return wrapper
    return decorator
