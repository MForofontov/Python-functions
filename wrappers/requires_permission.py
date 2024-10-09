from typing import Callable, Any

def requires_permission(permission: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(user_permissions: list[str], *args: Any, **kwargs: Any) -> Any:
            if permission not in user_permissions:
                raise PermissionError("User does not have the required permission.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
