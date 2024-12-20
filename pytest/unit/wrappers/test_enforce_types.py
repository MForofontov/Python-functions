import pytest
import logging
from typing import Any
from decorators.enforce_types import enforce_types

# Configure a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

@enforce_types(logger=test_logger)
def add(x: int, y: int) -> int:
    """
    Function that adds two integers.
    """
    return x + y

@enforce_types()
def greet(name: str) -> str:
    """
    Function that returns a greeting message.
    """
    return f"Hello, {name}!"

def test_add_correct_types():
    """
    Test the add function with correct types.
    """
    assert add(1, 2) == 3

def test_add_incorrect_types_logger(caplog):
    """
    Test the add function with incorrect types that writes to logger.
    """
    with caplog.at_level(logging.ERROR):
        add("1", 2)
        assert "Expected <class 'int'> for argument 'x', got <class 'str'>." in caplog.text

def test_greet_correct_type():
    """
    Test the greet function with correct type.
    """
    assert greet("world") == "Hello, world!"

def test_greet_incorrect_type_raise_error():
    """
    Test the greet function with incorrect type that raises error.
    """
    with pytest.raises(TypeError, match="Expected <class 'str'> for argument 'name', got <class 'int'>."):
        greet(123)

