import pytest
from decorators.conditional_execute import conditional_execute

# Example predicate functions
def always_true():
    return True

def always_false():
    return False

def predicate_based_on_args(a, b):
    return a > b

def predicate_based_on_kwargs(**kwargs):
    return kwargs.get('flag', False)

def predicate_based_on_mixed_args(a, b, **kwargs):
    return a > b and kwargs.get('flag', False)

def predicate_no_args():
    return True

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

@conditional_execute(lambda: predicate_based_on_kwargs(flag=True))
def example_function_kwargs(a, b, **kwargs):
    return f"Result: {a + b}"

@conditional_execute(lambda: predicate_based_on_mixed_args(3, 2, flag=True))
def example_function_mixed_args(a, b, **kwargs):
    return f"Result: {a + b}"

@conditional_execute(predicate_no_args)
def example_function_no_args(a, b):
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
    Test case 3: Predicate condition met based on arguments
    """
    # Test case 3: Predicate condition met based on arguments
    result = example_function_conditional(1, 2)
    assert result == "Result: 3"

def test_conditional_execute_condition_not_met():
    """
    Test case 4: Predicate condition not met based on arguments
    """
    # Test case 4: Predicate condition not met based on arguments
    @conditional_execute(lambda: predicate_based_on_args(1, 2))
    def example_function_conditional_not_met(a, b):
        return f"Result: {a + b}"
    
    result = example_function_conditional_not_met(1, 2)
    assert result is None

def test_conditional_execute_condition_met_kwargs():
    """
    Test case 5: Predicate condition met based on keyword arguments
    """
    # Test case 5: Predicate condition met based on keyword arguments
    result = example_function_kwargs(1, 2, flag=True)
    assert result == "Result: 3"

def test_conditional_execute_condition_not_met_kwargs():
    """
    Test case 6: Predicate condition not met based on keyword arguments
    """
    # Test case 6: Predicate condition not met based on keyword arguments
    @conditional_execute(lambda: predicate_based_on_kwargs(flag=False))
    def example_function_kwargs_not_met(a, b, **kwargs):
        return f"Result: {a + b}"
    
    result = example_function_kwargs_not_met(1, 2, flag=False)
    assert result is None

def test_conditional_execute_condition_met_mixed_args():
    """
    Test case 7: Predicate condition met based on mixed arguments and keyword arguments
    """
    # Test case 7: Predicate condition met based on mixed arguments and keyword arguments
    result = example_function_mixed_args(1, 2, flag=True)
    assert result == "Result: 3"

def test_conditional_execute_condition_not_met_mixed_args():
    """
    Test case 8: Predicate condition not met based on mixed arguments and keyword arguments
    """
    # Test case 8: Predicate condition not met based on mixed arguments and keyword arguments
    @conditional_execute(lambda: predicate_based_on_mixed_args(1, 2, flag=True))
    def example_function_mixed_args_not_met(a, b, **kwargs):
        return f"Result: {a + b}"
    
    result = example_function_mixed_args_not_met(1, 2, flag=True)
    assert result is None

def test_conditional_execute_no_args():
    """
    Test case 9: Predicate with no arguments
    """
    # Test case 9: Predicate with no arguments
    result = example_function_no_args(1, 2)
    assert result == "Result: 3"

def test_conditional_execute_with_default_args():
    """
    Test case 10: Function with default arguments
    """
    # Test case 10: Function with default arguments
    @conditional_execute(always_true)
    def example_function_default_args(a, b=0):
        return f"Result: {a + b}"
    
    result = example_function_default_args(3)
    assert result == "Result: 3"
    
    result = example_function_default_args(1, 2)
    assert result == "Result: 3"

def test_conditional_execute_predicate_raises_exception():
    """
    Test case 11: Predicate raises an exception
    """
    # Test case 11: Predicate raises an exception
    with pytest.raises(RuntimeError, match="Predicate function raised an error: Predicate raised an exception"):
        example_function_raises_exception(1, 2)

def test_conditional_execute_invalid_predicate():
    """
    Test case 12: Invalid predicate (not callable)
    """
    # Test case 12: Invalid predicate (not callable)
    with pytest.raises(TypeError, match="Predicate must be callable"):
        @conditional_execute("not a callable")
        def example_function_invalid(a, b):
            return f"Result: {a + b}"
