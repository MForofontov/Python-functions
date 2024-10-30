import pytest
from strings_utility.ljust_string import ljust_string

def test_ljust_string_default_fill() -> None:
    """
    Test the ljust_string function with the default fill character (space).
    """
    # Test case 1: Left-justify a string with default fill character (space)
    assert ljust_string("hello", 10) == 'hello     ', "Failed on default fill character"

def test_ljust_string_custom_fill() -> None:
    """
    Test the ljust_string function with a custom fill character.
    """
    # Test case 2: Left-justify a string with a custom fill character
    assert ljust_string("hello", 10, '-') == 'hello-----', "Failed on custom fill character"

def test_ljust_string_width_less_than_length() -> None:
    """
    Test the ljust_string function with width less than string length.
    """
    # Test case 3: Left-justify a string with width less than string length
    assert ljust_string("hello", 3) == 'hello', "Failed on width less than string length"

def test_ljust_string_width_equal_to_length() -> None:
    """
    Test the ljust_string function with width equal to string length.
    """
    # Test case 4: Left-justify a string with width equal to string length
    assert ljust_string("hello", 5) == 'hello', "Failed on width equal to string length"

def test_ljust_string_empty_string() -> None:
    """
    Test the ljust_string function with an empty string.
    """
    # Test case 5: Left-justify an empty string
    assert ljust_string("", 5) == '     ', "Failed on empty string"

def test_ljust_string_zero_width() -> None:
    """
    Test the ljust_string function with width of zero.
    """
    # Test case 6: Left-justify a string with width of zero
    assert ljust_string("hello", 0) == 'hello', "Failed on width of zero"

def test_ljust_string_negative_width() -> None:
    """
    Test the ljust_string function with width of negative value.
    """
    # Test case 7: Left-justify a string with width of negative value
    assert ljust_string("hello", -5) == 'hello', "Failed on negative width"

def test_ljust_string_even_width() -> None:
    """
    Test the ljust_string function with even width.
    """
    # Test case 8: Left-justify a string with even width
    assert ljust_string("hello", 10) == 'hello     ', "Failed on even width"

def test_ljust_string_odd_width() -> None:
    """
    Test the ljust_string function with odd width.
    """
    # Test case 9: Left-justify a string with odd width
    assert ljust_string("hello", 9) == 'hello    ', "Failed on odd width"

def test_ljust_string_multiple_custom_fill() -> None:
    """
    Test the ljust_string function with multiple custom fill characters.
    """
    # Test case 10: Left-justify a string with multiple custom fill characters
    assert ljust_string("hello", 10, '*') == 'hello*****', "Failed on multiple custom fill characters"

def test_ljust_string_single_character() -> None:
    """
    Test the ljust_string function with a single character.
    """
    # Test case 11: Left-justify a single character
    assert ljust_string("h", 5) == 'h    ', "Failed on single character"

def test_ljust_string_special_characters() -> None:
    """
    Test the ljust_string function with special characters.
    """
    # Test case 12: Left-justify a string with special characters
    assert ljust_string("!@#", 7) == '!@#    ', "Failed on special characters"

def test_ljust_string_numbers() -> None:
    """
    Test the ljust_string function with numbers.
    """
    # Test case 13: Left-justify a string with numbers
    assert ljust_string("12345", 10) == '12345     ', "Failed on numbers"

def test_ljust_string_mixed_characters() -> None:
    """
    Test the ljust_string function with mixed characters.
    """
    # Test case 14: Left-justify a string with mixed characters
    assert ljust_string("a1!b2@", 12) == 'a1!b2@      ', "Failed on mixed characters"

def test_ljust_string_leading_trailing_spaces() -> None:
    """
    Test the ljust_string function with leading and trailing spaces.
    """
    # Test case 15: Left-justify a string with leading and trailing spaces
    assert ljust_string("  hello  ", 15) == '  hello       ', "Failed on leading and trailing spaces"

def test_ljust_string_newline_characters() -> None:
    """
    Test the ljust_string function with newline characters.
    """
    # Test case 16: Left-justify a string with newline characters
    assert ljust_string("hello\nworld", 15) == 'hello\nworld   ', "Failed on newline characters"

def test_ljust_string_tab_characters() -> None:
    """
    Test the ljust_string function with tab characters.
    """
    # Test case 17: Left-justify a string with tab characters
    assert ljust_string("hello\tworld", 15) == 'hello\tworld   ', "Failed on tab characters"

def test_ljust_string_mixed_whitespace_characters() -> None:
    """
    Test the ljust_string function with mixed whitespace characters.
    """
    # Test case 18: Left-justify a string with mixed whitespace characters
    assert ljust_string("hello \t\nworld", 20) == 'hello \t\nworld       ', "Failed on mixed whitespace characters"

def test_ljust_string_non_english_characters() -> None:
    """
    Test the ljust_string function with non-English characters.
    """
    # Test case 19: Left-justify a string with non-English characters
    assert ljust_string("héllo wörld", 15) == 'héllo wörld    ', "Failed on non-English characters"

def test_ljust_string_invalid_string_type() -> None:
    """
    Test the ljust_string function with an invalid string type.
    """
    # Test case 20: Invalid string type
    with pytest.raises(TypeError):
        ljust_string(12345, 10)

def test_ljust_string_invalid_width_type() -> None:
    """
    Test the ljust_string function with an invalid width type.
    """
    # Test case 21: Invalid width type
    with pytest.raises(TypeError):
        ljust_string("hello", "10")

def test_ljust_string_invalid_fillchar_type() -> None:
    """
    Test the ljust_string function with an invalid fill character type.
    """
    # Test case 22: Invalid fill character type
    with pytest.raises(TypeError):
        ljust_string("hello", 10, 5)

def test_ljust_string_invalid_fillchar_length() -> None:
    """
    Test the ljust_string function with an invalid fill character length.
    """
    # Test case 23: Invalid fill character length
    with pytest.raises(TypeError):
        ljust_string("hello", 10, "ab")

if __name__ == "__main__":
    pytest.main()
