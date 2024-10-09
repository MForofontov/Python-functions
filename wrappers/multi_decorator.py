from typing import Callable, Any

def multi_decorator(*decorators: Callable[[Callable[..., Any]], Callable[..., Any]]) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def combine(func: Callable[..., Any]) -> Callable[..., Any]:
        for decorator in reversed(decorators):
            func = decorator(func)
        return func
    return combine
