import pytest
from decorators.chain import chain

class Chainable:
    def __init__(self, value: int):
        self.value = value

    def chain(self) -> int:
        return self.value * 2

class NonChainable:
    def __init__(self, value: int):
        self.value = value

@chain
def return_chainable(x: int) -> Chainable:
    return Chainable(x)

@chain
def return_non_chainable(x: int) -> NonChainable:
    return NonChainable(x)

@chain
def return_value(x: int) -> int:
    return x

def test_chain_with_chainable():
    result = return_chainable(5)
    assert result == 10  # Chainable.chain() should be called

def test_chain_with_non_chainable():
    result = return_non_chainable(5)
    assert isinstance(result, NonChainable)
    assert result.value == 5  # NonChainable.chain() should not be called

def test_chain_with_value():
    result = return_value(5)
    assert result == 5  # No chain method, should return the value directly

def test_chain_with_chainable_method_not_callable():
    class ChainableWithNonCallableChain:
        def __init__(self, value: int):
            self.value = value
            self.chain = "not callable"

    @chain
    def return_chainable_with_non_callable_chain(x: int) -> ChainableWithNonCallableChain:
        return ChainableWithNonCallableChain(x)

    result = return_chainable_with_non_callable_chain(5)
    assert isinstance(result, ChainableWithNonCallableChain)
    assert result.value == 5  # chain attribute is not callable, should return the object directly
