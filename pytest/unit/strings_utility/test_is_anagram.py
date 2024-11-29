import pytest
from strings_utility.is_anagram import is_anagram

def test_is_anagram_basic() -> None:
    """
    Test the is_anagram function with basic input.
    """
    # Test case 1: Basic anagram
    assert is_anagram("listen", "silent") == True, "Failed on basic anagram"

def test_is_anagram_with_spaces() -> None:
    """
    Test the is_anagram function with strings containing spaces.
    """
    # Test case 2: Anagram with spaces
    assert is_anagram("conversation", "voices rant on") == True, "Failed on anagram with spaces"

def test_is_anagram_with_different_cases() -> None:
    """
    Test the is_anagram function with strings containing different cases.
    """
    # Test case 3: Anagram with different cases
    assert is_anagram("Listen", "Silent") == True, "Failed on anagram with different cases"

def test_is_anagram_with_non_anagram() -> None:
    """
    Test the is_anagram function with non-anagram strings.
    """
    # Test case 4: Non-anagram strings
    assert is_anagram("hello", "world") == False, "Failed on non-anagram strings"

def test_is_anagram_with_empty_strings() -> None:
    """
    Test the is_anagram function with empty strings.
    """
    # Test case 5: Empty strings
    assert is_anagram("", "") == True, "Failed on empty strings"

def test_is_anagram_with_special_characters() -> None:
    """
    Test the is_anagram function with strings containing special characters.
    """
    # Test case 6: Anagram with special characters
    assert is_anagram("a!b@c#", "c@b!a#") == True, "Failed on anagram with special characters"

def test_is_anagram_with_numbers() -> None:
    """
    Test the is_anagram function with strings containing numbers.
    """
    # Test case 7: Anagram with numbers
    assert is_anagram("12345", "54321") == True, "Failed on anagram with numbers"

def test_is_anagram_with_unicode_characters() -> None:
    """
    Test the is_anagram function with strings containing unicode characters.
    """
    # Test case 8: Anagram with unicode characters
    assert is_anagram("déjà vu", "vu déjà") == True, "Failed on anagram with unicode characters"

def test_is_anagram_invalid_input_type() -> None:
    """
    Test the is_anagram function with invalid input types.
    """
    # Test case 9: Invalid input types
    with pytest.raises(TypeError):
        is_anagram(123, "silent")  # type: ignore
    with pytest.raises(TypeError):
        is_anagram("listen", 456)  # type: ignore
    with pytest.raises(TypeError):
        is_anagram(123, 456)  # type: ignore

def test_is_anagram_with_mixed_input() -> None:
    """
    Test the is_anagram function with mixed input types.
    """
    # Test case 10: Mixed input types
    with pytest.raises(TypeError):
        is_anagram("listen", None)  # type: ignore
    with pytest.raises(TypeError):
        is_anagram(None, "silent")  # type: ignore
    with pytest.raises(TypeError):
        is_anagram(None, None)  # type: ignore
