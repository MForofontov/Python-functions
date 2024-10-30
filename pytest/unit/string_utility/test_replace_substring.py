import pytest
from strings_utility.replace_substring import replace_substring

def test_replace_substring_basic() -> None:
    """
    Test the replace_substring function with a basic replacement.
    """
    # Test case 1: Basic replacement
    assert replace_substring("hello world", "world", "there") == "hello there", "Failed on basic replacement"

def test_replace_substring_multiple_occurrences() -> None:
    """
    Test the replace_substring function with multiple occurrences of the substring.
    """
    # Test case 2: Multiple occurrences
    assert replace_substring("a.b.c", ".", "-") == "a-b-c", "Failed on multiple occurrences"

def test_replace_substring_no_occurrences() -> None:
    """
    Test the replace_substring function when the substring does not occur.
    """
    # Test case 3: No occurrences
    assert replace_substring("hello world", "there", "world") == "hello world", "Failed on no occurrences"

def test_replace_substring_empty_string() -> None:
    """
    Test the replace_substring function with an empty string.
    """
    # Test case 4: Empty string
    assert replace_substring("", "a", "b") == "", "Failed on empty string"

def test_replace_substring_empty_old() -> None:
    """
    Test the replace_substring function with an empty old substring.
    """
    # Test case 5: Empty old substring
    assert replace_substring("hello world", "", "there") == "hello world", "Failed on empty old substring"

def test_replace_substring_empty_new() -> None:
    """
    Test the replace_substring function with an empty new substring.
    """
    # Test case 6: Empty new substring
    assert replace_substring("hello world", "world", "") == "hello ", "Failed on empty new substring"

def test_replace_substring_special_characters() -> None:
    """
    Test the replace_substring function with special characters.
    """
    # Test case 7: Special characters
    assert replace_substring("hello!@#world", "!@#", " ") == "hello world", "Failed on special characters"

def test_replace_substring_numbers() -> None:
    """
    Test the replace_substring function with numbers.
    """
    # Test case 8: Numbers
    assert replace_substring("123456", "123", "789") == "789456", "Failed on numbers"

def test_replace_substring_mixed_case() -> None:
    """
    Test the replace_substring function with mixed case substrings.
    """
    # Test case 9: Mixed case substrings
    assert replace_substring("Hello World", "World", "There") == "Hello There", "Failed on mixed case substrings"

def test_replace_substring_whitespace_characters() -> None:
    """
    Test the replace_substring function with whitespace characters.
    """
    # Test case 10: Whitespace characters
    assert replace_substring("hello world", " ", "-") == "hello-world", "Failed on whitespace characters"

def test_replace_substring_newline_characters() -> None:
    """
    Test the replace_substring function with newline characters.
    """
    # Test case 11: Newline characters
    assert replace_substring("hello\nworld", "\n", " ") == "hello world", "Failed on newline characters"

def test_replace_substring_tab_characters() -> None:
    """
    Test the replace_substring function with tab characters.
    """
    # Test case 12: Tab characters
    assert replace_substring("hello\tworld", "\t", " ") == "hello world", "Failed on tab characters"

def test_replace_substring_mixed_whitespace_characters() -> None:
    """
    Test the replace_substring function with mixed whitespace characters.
    """
    # Test case 13: Mixed whitespace characters
    assert replace_substring("hello \t\nworld", "\t\n", " ") == "hello world", "Failed on mixed whitespace characters"

def test_replace_substring_non_english_characters() -> None:
    """
    Test the replace_substring function with non-English characters.
    """
    # Test case 14: Non-English characters
    assert replace_substring("héllo wörld", "wörld", "world") == "héllo world", "Failed on non-English characters"

def test_replace_substring_invalid_string_type() -> None:
    """
    Test the replace_substring function with an invalid string type.
    """
    # Test case 15: Invalid string type
    with pytest.raises(TypeError):
        replace_substring(12345, "old", "new")

def test_replace_substring_invalid_old_type() -> None:
    """
    Test the replace_substring function with an invalid old substring type.
    """
    # Test case 16: Invalid old substring type
    with pytest.raises(TypeError):
        replace_substring("hello world", 123, "new")

def test_replace_substring_invalid_new_type() -> None:
    """
    Test the replace_substring function with an invalid new substring type.
    """
    # Test case 17: Invalid new substring type
    with pytest.raises(TypeError):
        replace_substring("hello world", "old", 123)

if __name__ == "__main__":
    pytest.main()
