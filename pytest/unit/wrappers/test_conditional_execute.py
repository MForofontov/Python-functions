import pytest
from decorators.conditional_execute import conditional_execute

# Predicate functions
def always_true() -> bool:
    """
    Predicate function that always returns True.
    
    Returns
    -------
    bool
        Always returns True.
    """
    return True

def always_false() -> bool:
    """
    Predicate function that always returns False.
    
    Returns
    -------
    bool
        Always returns False.
    """
    return False

@conditional_execute(always_true)
def add(x: int, y: int) -> int:
    """
    Function that adds two integers.
    """
    return x + y

@conditional_execute(always_false)
def multiply(x: int, y: int) -> int:
    """
    Function that multiplies two integers.
    """
    return x * y

@conditional_execute(always_true)
def greet_true(greeting: str, name: str = "world") -> str:
    """
    Function that returns a greeting message with a true predicate.
    """
    return f"{greeting}, {name}!"

@conditional_execute(always_false)
def greet_false(greeting: str, name: str = "world") -> str:
    """
    Function that returns a greeting message with a false predicate.
    """
    return f"{greeting}, {name}!"

def test_conditional_execute_add():
    """
    Test the conditional_execute decorator with the add function.
    """
    # Test case 1: Predicate returns True
    assert add(1, 2) == 3

def test_conditional_execute_multiply():
    """
    Test the conditional_execute decorator with the multiply function.
    """
    # Test case 2: Predicate returns False
    assert multiply(2, 3) is None

def test_conditional_execute_with_kwargs():
    """
    Test the conditional_execute decorator with keyword arguments.
    """
    # Test case 3: Keyword arguments with true predicate
    assert greet_true("Hello") == "Hello, world!"
    assert greet_true("Hello", name="Alice") == "Hello, Alice!"

def test_conditional_execute_with_false_predicate_and_kwargs():
    """
    Test the conditional_execute decorator with a false predicate and keyword arguments.
    """
    # Test case 4: Keyword arguments with false predicate
    assert greet_false("Hello") is None
    assert greet_false("Hello", name="Alice") is None

def test_conditional_execute_invalid_predicate():
    """
    Test the conditional_execute decorator with an invalid predicate.
    """
    # Test case 5: Invalid predicate
    with pytest.raises(TypeError, match="Predicate must be callable"):
        @conditional_execute("not a callable")
        def invalid_func(x: int) -> int:
            return x
