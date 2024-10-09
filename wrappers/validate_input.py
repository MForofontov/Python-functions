from typing import Callable, Any, Type

def validate_input(expected_type: Type) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(arg: Any) -> Any:
            if not isinstance(arg, expected_type):
                raise ValueError(f"Expected argument of type {expected_type}, got {type(arg)}")
            return func(arg)
        return wrapper
    return decorator
