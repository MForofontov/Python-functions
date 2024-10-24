import pytest
from strings_utility.ljust_string import ljust_string

def test_ljust_string() -> None:
    """
    Test the ljust_string function.

    This function tests the ljust_string function to ensure it correctly left-justifies
    a string in a field of a specified width using a specified fill character.
    """
    # Test case 1: Left-justify a string with default fill character (space)
    assert ljust_string("hello", 10) == 'hello     ', "Failed on default fill character"

    # Test case 2: Left-justify a string with a custom fill character
    assert ljust_string("hello", 10, '-') == 'hello-----', "Failed on custom fill character"

    # Test case 3: Left-justify a string with width less than string length
    assert ljust_string("hello", 3) == 'hello', "Failed on width less than string length"

    # Test case 4: Left-justify a string with width equal to string length
    assert ljust_string("hello", 5) == 'hello', "Failed on width equal to string length"

    # Test case 5: Left-justify an empty string
    assert ljust_string("", 5) == '     ', "Failed on empty string"

    # Test case 6: Left-justify a string with width of zero
    assert ljust_string("hello", 0) == 'hello', "Failed on width of zero"

    # Test case 7: Left-justify a string with width of negative value
    assert ljust_string("hello", -5) == 'hello', "Failed on negative width"

    # Test case 8: Left-justify a string with even width
    assert ljust_string("hello", 10) == 'hello     ', "Failed on even width"

    # Test case 9: Left-justify a string with odd width
    assert ljust_string("hello", 9) == 'hello    ', "Failed on odd width"

    # Test case 10: Left-justify a string with multiple custom fill characters
    assert ljust_string("hello", 10, '*') == 'hello*****', "Failed on multiple custom fill characters"

    # Test case 11: Left-justify a single character
    assert ljust_string("h", 5) == 'h    ', "Failed on single character"

    # Test case 12: Left-justify a string with special characters
    assert ljust_string("!@#", 7) == '!@#    ', "Failed on special characters"

    # Test case 13: Left-justify a string with numbers
    assert ljust_string("12345", 10) == '12345     ', "Failed on numbers"

    # Test case 14: Left-justify a string with mixed characters
    assert ljust_string("a1!b2@", 12) == 'a1!b2@      ', "Failed on mixed characters"

    # Test case 15: Left-justify a string with leading and trailing spaces
    assert ljust_string("  hello  ", 15) == '  hello       ', "Failed on leading and trailing spaces"

    # Test case 16: Left-justify a string with newline characters
    assert ljust_string("hello\nworld", 15) == 'hello\nworld   ', "Failed on newline characters"

    # Test case 17: Left-justify a string with tab characters
    assert ljust_string("hello\tworld", 15) == 'hello\tworld   ', "Failed on tab characters"

    # Test case 18: Left-justify a string with mixed whitespace characters
    assert ljust_string("hello \t\nworld", 20) == 'hello \t\nworld       ', "Failed on mixed whitespace characters"

    # Test case 19: Left-justify a string with non-English characters
    assert ljust_string("héllo wörld", 15) == 'héllo wörld    ', "Failed on non-English characters"

if __name__ == "__main__":
    pytest.main()