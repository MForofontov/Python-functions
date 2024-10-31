import pytest
from strings_utility.truncate_string_range import truncate_string_range

def test_truncate_string_range_basic() -> None:
    """
    Test the truncate_string_range function with basic truncation.
    """
    # Test case 1: Basic truncation
    assert truncate_string_range("hello world", 0, 5) == "hello", "Failed on basic truncation"

def test_truncate_string_range_middle() -> None:
    """
    Test the truncate_string_range function with truncation in the middle of the string.
    """
    # Test case 2: Truncation in the middle of the string
    assert truncate_string_range("hello world", 6, 11) == "world", "Failed on truncation in the middle of the string"

def test_truncate_string_range_end() -> None:
    """
    Test the truncate_string_range function with truncation at the end of the string.
    """
    # Test case 3: Truncation at the end of the string
    assert truncate_string_range("hello world", 6, 15) == "world", "Failed on truncation at the end of the string"

def test_truncate_string_range_out_of_bounds() -> None:
    """
    Test the truncate_string_range function with start and end indices out of bounds.
    """
    # Test case 4: Start and end indices out of bounds
    assert truncate_string_range("hello", 1, 10) == "ello", "Failed on start and end indices out of bounds"

def test_truncate_string_range_negative_indices() -> None:
    """
    Test the truncate_string_range function with negative indices.
    """
    # Test case 5: Negative indices
    assert truncate_string_range("hello world", -5, -1) == "worl", "Failed on negative indices"

def test_truncate_string_range_empty_string() -> None:
    """
    Test the truncate_string_range function with an empty string.
    """
    # Test case 6: Empty string
    assert truncate_string_range("", 0, 5) == "", "Failed on empty string"

def test_truncate_string_range_start_equals_end() -> None:
    """
    Test the truncate_string_range function with start index equal to end index.
    """
    # Test case 7: Start index equal to end index
    assert truncate_string_range("hello", 2, 2) == "", "Failed on start index equal to end index"

def test_truncate_string_range_start_greater_than_end() -> None:
    """
    Test the truncate_string_range function with start index greater than end index.
    """
    # Test case 8: Start index greater than end index
    assert truncate_string_range("hello", 3, 1) == "", "Failed on start index greater than end index"

def test_truncate_string_range_full_string() -> None:
    """
    Test the truncate_string_range function with the full string.
    """
    # Test case 9: Full string
    assert truncate_string_range("hello", 0, 5) == "hello", "Failed on full string"

def test_truncate_string_range_special_characters() -> None:
    """
    Test the truncate_string_range function with a string that contains special characters.
    """
    # Test case 10: String with special characters
    assert truncate_string_range("!@#hello$%^", 3, 8) == "hello", "Failed on string with special characters"

def test_truncate_string_range_numbers() -> None:
    """
    Test the truncate_string_range function with a string that contains numbers.
    """
    # Test case 11: String with numbers
    assert truncate_string_range("1234567890", 2, 5) == "345", "Failed on string with numbers"

def test_truncate_string_range_mixed_case() -> None:
    """
    Test the truncate_string_range function with a string that contains mixed case letters.
    """
    # Test case 12: String with mixed case letters
    assert truncate_string_range("HeLLoWoRLd", 2, 7) == "LLoWo", "Failed on string with mixed case letters"

def test_truncate_string_range_non_english_characters() -> None:
    """
    Test the truncate_string_range function with a string that contains non-English characters.
    """
    # Test case 13: String with non-English characters
    assert truncate_string_range("héllo wörld", 1, 9) == "éllo wör", "Failed on string with non-English characters"

def test_truncate_string_range_mixed_whitespace() -> None:
    """
    Test the truncate_string_range function with a string that contains mixed whitespace characters.
    """
    # Test case 14: String with mixed whitespace characters
    assert truncate_string_range(" \t\nhello world\t\n ", 3, 14) == "hello world", "Failed on string with mixed whitespace characters"

def test_truncate_string_range_invalid_string_type() -> None:
    """
    Test the truncate_string_range function with an invalid string type.
    """
    # Test case 15: Invalid string type
    with pytest.raises(TypeError):
        truncate_string_range(12345, 1, 3)

def test_truncate_string_range_invalid_start_type() -> None:
    """
    Test the truncate_string_range function with an invalid start index type.
    """
    # Test case 16: Invalid start index type
    with pytest.raises(TypeError):
        truncate_string_range("hello", "1", 3)

def test_truncate_string_range_invalid_end_type() -> None:
    """
    Test the truncate_string_range function with an invalid end index type.
    """
    # Test case 17: Invalid end index type
    with pytest.raises(TypeError):
        truncate_string_range("hello", 1, "3")

if __name__ == "__main__":
    pytest.main()
