from typing import Callable, Any
import time

def throttle(rate_limit: float) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        last_called = [0.0]

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_time = time.time()
            elapsed_time = current_time - last_called[0]
            if elapsed_time < rate_limit:
                time.sleep(rate_limit - elapsed_time)
            last_called[0] = time.time()
            return func(*args, **kwargs)

        return wrapper
    return decorator
