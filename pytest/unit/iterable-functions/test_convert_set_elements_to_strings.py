import pytest
from typing import Any
from iterable_functions.convert_set_elements_to_strings import convert_set_elements_to_strings

def test_convert_set_elements_to_strings_success() -> None:
    """
    Test the convert_set_elements_to_strings function with valid inputs.
    """
    # Test case 1: Valid inputs
    input_set: set[Any] = {1, 2, 3, 'a', 'b', 'c'}
    expected_output: set[str] = {'1', '2', '3', 'a', 'b', 'c'}
    assert convert_set_elements_to_strings(input_set) == expected_output

def test_convert_set_elements_to_strings_empty_set() -> None:
    """
    Test the convert_set_elements_to_strings function with an empty set.
    """
    # Test case 2: Empty set
    input_set: set[Any] = set()
    expected_output: set[str] = set()
    assert convert_set_elements_to_strings(input_set) == expected_output

def test_convert_set_elements_to_strings_type_error() -> None:
    """
    Test the convert_set_elements_to_strings function with invalid type for input_set.
    """
    # Test case 3: Invalid type for input_set
    with pytest.raises(TypeError):
        convert_set_elements_to_strings("not a set")

def test_convert_set_elements_to_strings_unconvertible_elements() -> None:
    """
    Test the convert_set_elements_to_strings function with elements that cannot be converted to strings.
    """
    # Test case 4: Elements that cannot be converted to strings
    input_set: set[Any] = {1, 2, 3, 'a', 'b', 'c', object()}
    with pytest.raises(TypeError):
        convert_set_elements_to_strings(input_set)