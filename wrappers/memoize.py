from typing import Callable, Any, Dict, Tuple

def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict[Tuple] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper
