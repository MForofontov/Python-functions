from typing import Callable, Any, Dict, Tuple
import time

def memoize_with_expiration(expiration_time: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        cache: Dict[Tuple, Tuple[float, Any]] = {}
        
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            if key in cache:
                cached_time, cached_value = cache[key]
                if current_time - cached_time < expiration_time:
                    return cached_value
            result = func(*args, **kwargs)
            cache[key] = (current_time, result)
            return result
        
        return wrapper
    return decorator
