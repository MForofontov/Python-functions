import pytest
from conditional_return import conditional_return

# Example condition functions
def always_true(*args, **kwargs):
    return True

def always_false(*args, **kwargs):
    return False

def condition_based_on_args(a, b):
    return a > b

# Example functions to be decorated
@conditional_return(always_true, "Condition met")
def example_function_true(a, b):
    return f"Result: {a + b}"

@conditional_return(always_false, "Condition met")
def example_function_false(a, b):
    return f"Result: {a + b}"

@conditional_return(condition_based_on_args, "Condition met")
def example_function_conditional(a, b):
    return f"Result: {a + b}"

def test_conditional_return_always_true():
    """
    Test case 1: Condition always true
    """
    result = example_function_true(1, 2)
    assert result == "Condition met"

def test_conditional_return_always_false():
    """
    Test case 2: Condition always false
    """
    result = example_function_false(1, 2)
    assert result == "Result: 3"

def test_conditional_return_condition_met():
    """
    Test case 3: Condition met based on arguments
    """
    result = example_function_conditional(3, 2)
    assert result == "Condition met"

def test_conditional_return_condition_not_met():
    """
    Test case 4: Condition not met based on arguments
    """
    result = example_function_conditional(1, 2)
    assert result == "Result: 3"

def test_conditional_return_with_kwargs():
    """
    Test case 5: Condition with keyword arguments
    """
    @conditional_return(lambda a, b: a > b, "Condition met")
    def example_function_kwargs(a, b=0):
        return f"Result: {a + b}"
    
    result = example_function_kwargs(a=3, b=2)
    assert result == "Condition met"
    
    result = example_function_kwargs(a=1, b=2)
    assert result == "Result: 3"

def test_conditional_return_invalid_condition():
    """
    Test case 6: Invalid condition (not callable)
    """
    with pytest.raises(TypeError, match="Condition must be callable"):
        @conditional_return("not a callable", "Condition met")
        def example_function_invalid(a, b):
            return f"Result: {a + b}"

def test_conditional_return_no_args():
    """
    Test case 7: Function with no arguments
    """
    @conditional_return(always_true, "Condition met")
    def example_function_no_args():
        return "Original result"
    
    result = example_function_no_args()
    assert result == "Condition met"

def test_conditional_return_with_default_args():
    """
    Test case 8: Function with default arguments
    """
    @conditional_return(lambda a, b=0: a > b, "Condition met")
    def example_function_default_args(a, b=0):
        return f"Result: {a + b}"
    
    result = example_function_default_args(3)
    assert result == "Condition met"
    
    result = example_function_default_args(1, 2)
    assert result == "Result: 3"
