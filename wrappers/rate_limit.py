from typing import Callable, Any
import time

def rate_limit(max_calls: int, period: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        calls = []
        
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal calls
            current_time = time.time()
            calls = [call for call in calls if current_time - call < period]
            
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded. Try again later.")
                
            calls.append(current_time)
            return func(*args, **kwargs)

        return wrapper
    return decorator
