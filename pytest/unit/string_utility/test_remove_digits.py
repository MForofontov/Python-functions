import pytest
from strings_utility.remove_digits import remove_digits

def test_remove_digits_mixed_characters() -> None:
    """
    Test the remove_digits function with a string that contains both letters and digits.
    """
    # Test case 1: String with mixed letters and digits
    assert remove_digits("abc123") == "abc", "Failed on mixed letters and digits"

def test_remove_digits_only_digits() -> None:
    """
    Test the remove_digits function with a string that contains only digits.
    """
    # Test case 2: String with only digits
    assert remove_digits("12345") == "", "Failed on string with only digits"

def test_remove_digits_only_letters() -> None:
    """
    Test the remove_digits function with a string that contains only letters.
    """
    # Test case 3: String with only letters
    assert remove_digits("abcdef") == "abcdef", "Failed on string with only letters"

def test_remove_digits_empty_string() -> None:
    """
    Test the remove_digits function with an empty string.
    """
    # Test case 4: Empty string
    assert remove_digits("") == "", "Failed on empty string"

def test_remove_digits_special_characters() -> None:
    """
    Test the remove_digits function with a string that contains special characters.
    """
    # Test case 5: String with special characters
    assert remove_digits("abc!@#123") == "abc!@#", "Failed on string with special characters"

def test_remove_digits_whitespace_characters() -> None:
    """
    Test the remove_digits function with a string that contains whitespace characters.
    """
    # Test case 6: String with whitespace characters
    assert remove_digits("abc 123 def") == "abc  def", "Failed on string with whitespace characters"

def test_remove_digits_newline_characters() -> None:
    """
    Test the remove_digits function with a string that contains newline characters.
    """
    # Test case 7: String with newline characters
    assert remove_digits("abc\n123\ndef") == "abc\ndef", "Failed on string with newline characters"

def test_remove_digits_tab_characters() -> None:
    """
    Test the remove_digits function with a string that contains tab characters.
    """
    # Test case 8: String with tab characters
    assert remove_digits("abc\t123\tdef") == "abc\tdef", "Failed on string with tab characters"

def test_remove_digits_mixed_whitespace_characters() -> None:
    """
    Test the remove_digits function with a string that contains mixed whitespace characters.
    """
    # Test case 9: String with mixed whitespace characters
    assert remove_digits("abc \t\n123 \t\ndef") == "abc \t\ndef", "Failed on string with mixed whitespace characters"

def test_remove_digits_leading_trailing_spaces() -> None:
    """
    Test the remove_digits function with a string that contains leading and trailing spaces.
    """
    # Test case 10: String with leading and trailing spaces
    assert remove_digits(" 123 abc 456 ") == " abc ", "Failed on string with leading and trailing spaces"

def test_remove_digits_non_english_characters() -> None:
    """
    Test the remove_digits function with a string that contains non-English characters.
    """
    # Test case 11: String with non-English characters
    assert remove_digits("héllo123 wörld456") == "héllo wörld", "Failed on string with non-English characters"

def test_remove_digits_mixed_case() -> None:
    """
    Test the remove_digits function with a string that contains mixed case letters.
    """
    # Test case 12: String with mixed case letters
    assert remove_digits("AbC123dEf456") == "AbCdEf", "Failed on string with mixed case letters"

def test_remove_digits_numbers_within_words() -> None:
    """
    Test the remove_digits function with a string that contains numbers within words.
    """
    # Test case 13: String with numbers within words
    assert remove_digits("a1b2c3") == "abc", "Failed on string with numbers within words"

def test_remove_digits_numbers_at_start_and_end() -> None:
    """
    Test the remove_digits function with a string that contains numbers at the start and end.
    """
    # Test case 14: String with numbers at the start and end
    assert remove_digits("123abc456") == "abc", "Failed on string with numbers at the start and end"

def test_remove_non_alphanumeric_invalid_type() -> None:
    """
    Test the remove_non_alphanumeric function with an invalid type.
    """
    # Test case 15: Invalid type
    with pytest.raises(TypeError):
        remove_digits(123)

if __name__ == "__main__":
    pytest.main()
