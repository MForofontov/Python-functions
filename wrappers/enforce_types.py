from typing import Callable, Any, get_type_hints

def enforce_types(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        hints = get_type_hints(func)
        for arg_name, arg_value in zip(hints.keys(), args):
            expected_type = hints[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Expected {expected_type} for argument '{arg_name}', got {type(arg_value)}.")
        return func(*args, **kwargs)
    return wrapper
