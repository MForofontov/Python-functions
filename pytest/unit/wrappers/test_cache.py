import pytest
from decorators.cache import cache

# Dictionary to keep track of function execution counts
execution_count = {
    "add": 0,
    "multiply": 0,
    "concat_strings": 0,
    "greet": 0
}

@cache
def add(x: int, y: int) -> int:
    """
    Function that adds two integers.
    """
    execution_count["add"] += 1
    return x + y

@cache
def multiply(x: int, y: int) -> int:
    """
    Function that multiplies two integers.
    """
    execution_count["multiply"] += 1
    return x * y

@cache
def concat_strings(a: str, b: str) -> str:
    """
    Function that concatenates two strings.
    """
    execution_count["concat_strings"] += 1
    return a + b

def test_cache_add():
    """
    Test the cache decorator with the add function.
    """
    # Test case 1: Add function
    assert add(1, 2) == 3
    assert add(1, 2) == 3  # Cached result
    assert execution_count["add"] == 1  # Should only be executed once

def test_cache_multiply():
    """
    Test the cache decorator with the multiply function.
    """
    # Test case 2: Multiply function
    assert multiply(2, 3) == 6
    assert multiply(2, 3) == 6  # Cached result
    assert execution_count["multiply"] == 1  # Should only be executed once

def test_cache_concat_strings():
    """
    Test the cache decorator with the concat_strings function.
    """
    # Test case 3: Concat strings function
    assert concat_strings("hello", "world") == "helloworld"
    assert concat_strings("hello", "world") == "helloworld"  # Cached result
    assert execution_count["concat_strings"] == 1  # Should only be executed once

def test_cache_different_args():
    """
    Test the cache decorator with different arguments.
    """
    # Test case 4: Different arguments
    assert add(2, 3) == 5
    assert add(2, 3) == 5  # Cached result
    assert add(3, 2) == 5  # Different arguments, not cached
    assert execution_count["add"] == 2  # Should be executed twice

def test_cache_with_kwargs():
    """
    Test the cache decorator with keyword arguments.
    """
    # Test case 5: Keyword arguments
    @cache
    def greet(greeting: str, name: str = "world") -> str:
        """
        Function that returns a greeting message.
        """
        execution_count["greet"] += 1
        return f"{greeting}, {name}!"

    assert greet("Hello") == "Hello, world!"
    assert greet("Hello") == "Hello, world!"  # Cached result
    assert greet("Hello", name="Alice") == "Hello, Alice!"
    assert greet("Hello", name="Alice") == "Hello, Alice!"  # Cached result
    assert execution_count["greet"] == 2  # Should be executed twice
