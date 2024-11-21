import pytest
from iterable_functions.try_convert_to_type import try_convert_to_type

def test_try_convert_to_type_success_int() -> None:
    """
    Test the try_convert_to_type function with valid integer conversion.
    """
    value = "123"
    target_type = int
    expected_output = 123
    assert try_convert_to_type(value, target_type) == expected_output

def test_try_convert_to_type_success_float() -> None:
    """
    Test the try_convert_to_type function with valid float conversion.
    """
    value = "123.45"
    target_type = float
    expected_output = 123.45
    assert try_convert_to_type(value, target_type) == expected_output

def test_try_convert_to_type_success_str() -> None:
    """
    Test the try_convert_to_type function with valid string conversion.
    """
    value = 123
    target_type = str
    expected_output = "123"
    assert try_convert_to_type(value, target_type) == expected_output

def test_try_convert_to_type_invalid_conversion() -> None:
    """
    Test the try_convert_to_type function with an invalid conversion.
    """
    value = "abc"
    target_type = int
    with pytest.raises(ValueError):
        try_convert_to_type(value, target_type)

def test_try_convert_to_type_type_error() -> None:
    """
    Test the try_convert_to_type function with invalid type for target_type.
    """
    with pytest.raises(TypeError):
        try_convert_to_type("123", "not a type")
