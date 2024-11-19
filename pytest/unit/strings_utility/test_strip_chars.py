import pytest
from strings_utility.strip_chars import strip_chars

def test_strip_chars_single_character() -> None:
    """
    Test the strip_chars function with a single character to strip.
    """
    # Test case 1: Single character strip
    assert strip_chars("...hello...", ".") == "hello", "Failed on single character strip"

def test_strip_chars_multiple_characters() -> None:
    """
    Test the strip_chars function with multiple characters to strip.
    """
    # Test case 2: Multiple characters strip
    assert strip_chars("xyzhellozyx", "xyz") == "hello", "Failed on multiple characters strip"

def test_strip_chars_no_match() -> None:
    """
    Test the strip_chars function when there are no matching characters to strip.
    """
    # Test case 3: No matching characters to strip
    assert strip_chars("hello", "xyz") == "hello", "Failed on no matching characters to strip"

def test_strip_chars_empty_string() -> None:
    """
    Test the strip_chars function with an empty string.
    """
    # Test case 4: Empty string
    assert strip_chars("", "xyz") == "", "Failed on empty string"

def test_strip_chars_no_chars_argument() -> None:
    """
    Test the strip_chars function with an empty chars argument.
    """
    # Test case 5: Empty chars argument
    assert strip_chars("hello", "") == "hello", "Failed on empty chars argument"

def test_strip_chars_all_match() -> None:
    """
    Test the strip_chars function when all characters match the strip characters.
    """
    # Test case 6: All characters match strip characters
    assert strip_chars("aaaa", "a") == "", "Failed when all characters match strip characters"

def test_strip_chars_special_characters() -> None:
    """
    Test the strip_chars function with special characters.
    """
    # Test case 7: Special character strip
    assert strip_chars("!!!hello!!!", "!") == "hello", "Failed on special character strip"

def test_strip_chars_leading_and_trailing() -> None:
    """
    Test the strip_chars function with both leading and trailing characters to strip.
    """
    # Test case 8: Leading and trailing characters
    assert strip_chars("///hello///", "/") == "hello", "Failed on leading and trailing characters"

def test_strip_chars_numbers_and_letters() -> None:
    """
    Test the strip_chars function with a mix of numbers and letters to strip.
    """
    # Test case 9: Numbers and letters mix
    assert strip_chars("123abc123", "123") == "abc", "Failed on numbers and letters mix"

def test_strip_chars_unicode_characters() -> None:
    """
    Test the strip_chars function with unicode characters to strip.
    """
    # Test case 10: Unicode characters
    assert strip_chars("😊😊hello😊😊", "😊") == "hello", "Failed on unicode characters"

def test_strip_chars_mixed_whitespace() -> None:
    """
    Test the strip_chars function with mixed whitespace to strip.
    """
    # Test case 11: Mixed whitespace
    assert strip_chars("   \thello   ", " \t") == "hello", "Failed on mixed whitespace"

def test_strip_chars_only_spaces() -> None:
    """
    Test the strip_chars function when the input string is only spaces.
    """
    # Test case 12: Input string with only spaces
    assert strip_chars("     ", " ") == "", "Failed on input string with only spaces"

def test_strip_chars_only_numbers() -> None:
    """
    Test the strip_chars function with a string of only numbers.
    """
    # Test case 13: String of only numbers
    assert strip_chars("123456789", "123") == "456789", "Failed on string of only numbers"

def test_strip_chars_partial_match() -> None:
    """
    Test the strip_chars function when only part of the string matches.
    """
    # Test case 14: Partial match
    assert strip_chars("abcdef", "def") == "abc", "Failed on partial match"

def test_strip_chars_partial_non_match() -> None:
    """
    Test the strip_chars function when chars partially overlap but don't match fully.
    """
    # Test case 15: Partial non-match
    assert strip_chars("abccba", "a") == "bccb", "Failed on partial non-match"

def test_strip_chars_strip_same_as_string() -> None:
    """
    Test the strip_chars function when the chars to strip are the same as the string.
    """
    # Test case 16: Chars to strip are the same as string
    assert strip_chars("xyz", "xyz") == "", "Failed when chars to strip are the same as string"

def test_strip_chars_alphanumeric() -> None:
    """
    Test the strip_chars function with a mix of alphanumeric characters to strip.
    """
    # Test case 17: Alphanumeric mix
    assert strip_chars("123abc456", "123456") == "abc", "Failed on alphanumeric mix"

def test_strip_chars_substring_in_middle() -> None:
    """
    Test the strip_chars function when the strip characters appear in the middle of the string.
    """
    # Test case 18: Substring in middle
    assert strip_chars("hello123world", "world") == "hello123", "Failed on substring in middle"

def test_strip_chars_case_sensitivity() -> None:
    """
    Test the strip_chars function for case sensitivity in chars to strip.
    """
    # Test case 19: Case sensitivity
    assert strip_chars("aAaHello", "a") == "AaHello", "Failed on case sensitivity"

def test_strip_chars_with_escapes() -> None:
    """
    Test the strip_chars function when chars include escape characters.
    """
    # Test case 20: Escape characters
    assert strip_chars("\n\tHello", "\n\t") == "Hello", "Failed on escape characters"

def test_strip_chars_invalid_string_type() -> None:
    """
    Test the strip_chars function with an invalid string type.
    """
    # Test case 21: Invalid string type
    with pytest.raises(TypeError):
        strip_chars(12345, "xyz")

def test_strip_chars_invalid_chars_type() -> None:
    """
    Test the strip_chars function with an invalid chars type.
    """
    # Test case 22: Invalid chars type
    with pytest.raises(TypeError):
        strip_chars("hello", 123)

