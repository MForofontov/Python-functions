from typing import Callable, Any
import json

def serialize_output(format: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)
            if format == 'json':
                return json.dumps(result)
            return str(result)
        return wrapper
    return decorator
