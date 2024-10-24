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

    # Test case 8: Center a string with even width
    assert center_string("hello", 10) == '  hello   ', "Failed on even width"

    # Test case 9: Center a string with odd width
    assert center_string("hello", 9) == '  hello  ', "Failed on odd width"

    # Test case 10: Center a string with multiple custom fill characters
    assert center_string("hello", 11, '*') == '***hello***', "Failed on multiple custom fill characters"

    # Test case 11: Center a string with a single character
    assert center_string("h", 5) == '  h  ', "Failed on single character"

    # Test case 12: Center a string with special characters
    assert center_string("!@#", 7) == '  !@#  ', "Failed on special characters"

    # Test case 13: Center a string with numbers
    assert center_string("12345", 10) == '  12345   ', "Failed on numbers"

    # Test case 14: Center a string with mixed characters
    assert center_string("a1!b2@", 12) == '   a1!b2@   ', "Failed on mixed characters"

    # Test case 15: Center a string with leading and trailing spaces
    assert center_string("  hello  ", 15) == '    hello     ', "Failed on leading and trailing spaces"

    # Test case 16: Center a string with newline characters
    assert center_string("hello\nworld", 15) == '  hello\nworld  ', "Failed on newline characters"

    # Test case 17: Center a string with tab characters
    assert center_string("hello\tworld", 15) == '  hello\tworld  ', "Failed on tab characters"

    # Test case 18: Center a string with mixed whitespace characters
    assert center_string("hello \t\nworld", 20) == '   hello \t\nworld    ', "Failed on mixed whitespace characters"

if __name__ == "__main__":
    pytest.main()