import pytest
from decorators.cache import cache

execution_count = {
    "add": 0,
    "multiply": 0,
    "concat_strings": 0,
    "greet": 0
}

@cache
def add(x, y):
    execution_count["add"] += 1
    return x + y

@cache
def multiply(x, y):
    execution_count["multiply"] += 1
    return x * y

@cache
def concat_strings(a: str, b: str) -> str:
    execution_count["concat_strings"] += 1
    return a + b

def test_cache_add():
    assert add(1, 2) == 3
    assert add(1, 2) == 3  # Cached result
    assert execution_count["add"] == 1  # Should only be executed once

def test_cache_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, 3) == 6  # Cached result
    assert execution_count["multiply"] == 1  # Should only be executed once

def test_cache_concat_strings():
    assert concat_strings("hello", "world") == "helloworld"
    assert concat_strings("hello", "world") == "helloworld"  # Cached result
    assert execution_count["concat_strings"] == 1  # Should only be executed once

def test_cache_different_args():
    assert add(2, 3) == 5
    assert add(2, 3) == 5  # Cached result
    assert add(3, 2) == 5  # Different arguments, not cached
    assert execution_count["add"] == 2  # Should be executed twice

def test_cache_with_kwargs():
    @cache
    def greet(greeting, name="world"):
        execution_count["greet"] += 1
        return f"{greeting}, {name}!"

    assert greet("Hello") == "Hello, world!"
    assert greet("Hello") == "Hello, world!"  # Cached result
    assert greet("Hello", name="Alice") == "Hello, Alice!"
    assert greet("Hello", name="Alice") == "Hello, Alice!"  # Cached result
    assert execution_count["greet"] == 2  # Should be executed twice
    