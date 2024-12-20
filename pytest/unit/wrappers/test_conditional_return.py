import pytest
from decorators.conditional_return import conditional_return

# Condition functions
def always_true(*args, **kwargs) -> bool:
    """
    Condition function that always returns True.
    
    Returns
    -------
    bool
        Always returns True.
    """
    return True

def always_false(*args, **kwargs) -> bool:
    """
    Condition function that always returns False.
    
    Returns
    -------
    bool
        Always returns False.
    """
    return False

def condition_based_on_args(x: int, y: int) -> bool:
    """
    Condition function that returns True if x is greater than y.
    
    Parameters
    ----------
    x : int
        First integer.
    y : int
        Second integer.
    
    Returns
    -------
    bool
        True if x is greater than y, otherwise False.
    """
    return x > y

@conditional_return(always_true, return_value=42)
def add(x: int, y: int) -> int:
    """
    Function that adds two integers.
    """
    return x + y

@conditional_return(always_false, return_value=42)
def multiply(x: int, y: int) -> int:
    """
    Function that multiplies two integers.
    """
    return x * y

@conditional_return(condition_based_on_args, return_value="x is greater")
def compare(x: int, y: int) -> str:
    """
    Function that compares two integers.
    """
    return "x is not greater"

def test_conditional_return_add():
    """
    Test the conditional_return decorator with the add function.
    """
    # Test case 1: Condition always returns True
    assert add(1, 2) == 42

def test_conditional_return_multiply():
    """
    Test the conditional_return decorator with the multiply function.
    """
    # Test case 2: Condition always returns False
    assert multiply(2, 3) == 6

def test_conditional_return_compare():
    """
    Test the conditional_return decorator with the compare function.
    """
    # Test case 3: Condition based on arguments
    assert compare(5, 3) == "x is greater"
    assert compare(2, 4) == "x is not greater"

def test_conditional_return_invalid_condition():
    """
    Test the conditional_return decorator with an invalid condition.
    """
    # Test case 4: Invalid condition
    with pytest.raises(TypeError, match="Condition must be callable"):
        @conditional_return("not a callable", return_value=42)
        def invalid_func(x: int) -> int:
            return x
