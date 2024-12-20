import pytest
from decorators.chain import chain

class Chainable:
    """
    A class that has a chain method which doubles its value.
    """
    def __init__(self, value: int):
        self.value = value

    def chain(self) -> int:
        """
        Method to double the value.
        """
        return self.value * 2

class NonChainable:
    """
    A class that does not have a chain method.
    """
    def __init__(self, value: int):
        self.value = value

@chain
def return_chainable(x: int) -> Chainable:
    """
    Function that returns a Chainable object.
    """
    return Chainable(x)

@chain
def return_non_chainable(x: int) -> NonChainable:
    """
    Function that returns a NonChainable object.
    """
    return NonChainable(x)

@chain
def return_value(x: int) -> int:
    """
    Function that returns a simple integer value.
    """
    return x

def test_chain_with_chainable():
    """
    Test the chain decorator with a Chainable object.
    """
    # Test case 1: Chainable object
    result = return_chainable(5)
    assert result == 10  # Chainable.chain() should be called

def test_chain_with_non_chainable():
    """
    Test the chain decorator with a NonChainable object.
    """
    # Test case 2: NonChainable object
    result = return_non_chainable(5)
    assert isinstance(result, NonChainable)
    assert result.value == 5  # NonChainable.chain() should not be called

def test_chain_with_value():
    """
    Test the chain decorator with a simple value.
    """
    # Test case 3: Simple value
    result = return_value(5)
    assert result == 5  # No chain method, should return the value directly

def test_chain_with_chainable_method_not_callable():
    """
    Test the chain decorator with a Chainable object that has a non-callable chain attribute.
    """
    # Test case 4: Chainable object with non-callable chain attribute
    class ChainableWithNonCallableChain:
        """
        A class that has a non-callable chain attribute.
        """
        def __init__(self, value: int):
            self.value = value
            self.chain = "not callable"

    @chain
    def return_chainable_with_non_callable_chain(x: int) -> ChainableWithNonCallableChain:
        """
        Function that returns a ChainableWithNonCallableChain object.
        """
        return ChainableWithNonCallableChain(x)

    result = return_chainable_with_non_callable_chain(5)
    assert isinstance(result, ChainableWithNonCallableChain)
    assert result.value == 5  # chain attribute is not callable, should return the object directly

def test_chain_invalid_function():
    """
    Test the chain decorator with an invalid function.
    """
    # Test case 5: Invalid function
    with pytest.raises(TypeError, match="The function to be wrapped must be callable"):
        @chain("not a callable")
        def invalid_func(x: int) -> int:
            return x
