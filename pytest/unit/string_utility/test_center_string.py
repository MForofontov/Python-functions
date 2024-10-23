import pytest
from strings_utility.center_string import center_string

def test_center_string() -> None:
    """
    Test the center_string function.

    This function tests the center_string function to ensure it correctly centers
    a string within a specified width using a specified fill character.
    """
    # Test case 1: Center a string with default fill character (space)
    assert center_string("hello", 11) == '   hello   ', "Failed on default fill character"

    # Test case 2: Center a string with a custom fill character
    assert center_string("hello", 11, '-') == '---hello---', "Failed on custom fill character"

    # Test case 3: Center a string with width less than string length
    assert center_string("hello", 3) == 'hello', "Failed on width less than string length"

    # Test case 4: Center a string with width equal to string length
    assert center_string("hello", 5) == 'hello', "Failed on width equal to string length"

    # Test case 5: Center a string with an empty string
    assert center_string("", 5) == '     ', "Failed on empty string"

    # Test case 6: Center a string with width of zero
    assert center_string("hello", 0) == 'hello', "Failed on width of zero"

    # Test case 7: Center a string with width of negative value
    assert center_string("hello", -5) == 'hello', "Failed on negative width"

if __name__ == "__main__":
    pytest.main()