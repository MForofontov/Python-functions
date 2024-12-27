import pytest
from conditional_execute import conditional_execute

# Example predicate functions
def always_true():
    return True

def always_false():
    return False

def predicate_based_on_args(a, b):
    return a > b

def predicate_raises_exception():
    raise ValueError("Predicate raised an exception")

# Example functions to be decorated
@conditional_execute(always_true)
def example_function_true(a, b):
    return f"Result: {a + b}"

@conditional_execute(always_false)
def example_function_false(a, b):
    return f"Result: {a + b}"

@conditional_execute(lambda: predicate_based_on_args(3, 2))
def example_function_conditional(a, b):
    return f"Result: {a + b}"

@conditional_execute(predicate_raises_exception)
def example_function_raises_exception(a, b):
    return f"Result: {a + b}"

def test_conditional_execute_always_true():
    """
    Test case 1: Predicate always true
    """
    # Test case 1: Predicate always true
    result = example_function_true(1, 2)
    assert result == "Result: 3"

def test_conditional_execute_always_false():
    """
    Test case 2: Predicate always false
    """
    # Test case 2: Predicate always false
    result = example_function_false(1, 2)
    assert result is None

def test_conditional_execute_condition_met():
    """
    Test case 3: Predicate condition met
    """
    # Test case 3: Predicate condition met
    result = example_function_conditional(1, 2)
    assert result == "Result: 3"

def test_conditional_execute_condition_not_met():
    """
    Test case 4: Predicate condition not met
    """
    # Test case 4: Predicate condition not met
    @conditional_execute(lambda: predicate_based_on_args(1, 2))
    def example_function_conditional_not_met(a, b):
        return f"Result: {a + b}"
    
    result = example_function_conditional_not_met(1, 2)
    assert result is None

def test_conditional_execute_no_args():
    """
    Test case 5: Function with no arguments
    """
    # Test case 5: Function with no arguments
    @conditional_execute(always_true)
    def example_function_no_args():
        return "Original result"
    
    result = example_function_no_args()
    assert result == "Original result"

def test_conditional_execute_with_default_args():
    """
    Test case 6: Function with default arguments
    """
    # Test case 6: Function with default arguments
    @conditional_execute(always_true)
    def example_function_default_args(a, b=0):
        return f"Result: {a + b}"
    
    result = example_function_default_args(3)
    assert result == "Result: 3"
    
    result = example_function_default_args(1, 2)
    assert result == "Result: 3"

def test_conditional_execute_predicate_raises_exception():
    """
    Test case 7: Predicate raises an exception
    """
    # Test case 7: Predicate raises an exception
    with pytest.raises(RuntimeError, match="Predicate function raised an error: Predicate raised an exception"):
        example_function_raises_exception(1, 2)

def test_conditional_execute_invalid_predicate():
    """
    Test case 8: Invalid predicate (not callable)
    """
    # Test case 8: Invalid predicate (not callable)
    with pytest.raises(TypeError, match="Predicate must be callable"):
        @conditional_execute("not a callable")
        def example_function_invalid(a, b):
            return f"Result: {a + b}"
