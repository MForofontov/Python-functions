import pytest
from strings_utility.ends_with import ends_with

def test_ends_with() -> None:
    """
    Test the ends_with function.

    This function tests the ends_with function to ensure it correctly checks
    if a string ends with a specified suffix.
    """
    # Test case 1: String ends with the suffix
    assert ends_with("hello world", "world") == True, "Failed on string ending with suffix"

    # Test case 2: String does not end with the suffix
    assert ends_with("hello world", "hello") == False, "Failed on string not ending with suffix"

    # Test case 3: Suffix is the entire string
    assert ends_with("hello", "hello") == True, "Failed on suffix being the entire string"

    # Test case 4: Empty suffix
    assert ends_with("hello", "") == True, "Failed on empty suffix"

    # Test case 5: Empty string and non-empty suffix
    assert ends_with("", "hello") == False, "Failed on empty string and non-empty suffix"

    # Test case 6: Both string and suffix are empty
    assert ends_with("", "") == True, "Failed on both string and suffix being empty"

    # Test case 7: Suffix longer than string
    assert ends_with("hello", "hello world") == False, "Failed on suffix longer than string"

    # Test case 8: String ends with special characters
    assert ends_with("hello!@#", "!@#") == True, "Failed on string ending with special characters"

    # Test case 9: String does not end with special characters
    assert ends_with("hello!@#", "@!") == False, "Failed on string not ending with special characters"

    # Test case 10: String ends with a space
    assert ends_with("hello world ", " ") == True, "Failed on string ending with a space"

    # Test case 11: String does not end with a space
    assert ends_with("hello world", " ") == False, "Failed on string not ending with a space"

    # Test case 12: String ends with a newline character
    assert ends_with("hello world\n", "\n") == True, "Failed on string ending with a newline character"

    # Test case 13: String does not end with a newline character
    assert ends_with("hello world", "\n") == False, "Failed on string not ending with a newline character"

    # Test case 14: String ends with a tab character
    assert ends_with("hello world\t", "\t") == True, "Failed on string ending with a tab character"

    # Test case 15: String does not end with a tab character
    assert ends_with("hello world", "\t") == False, "Failed on string not ending with a tab character"

    # Test case 16: String ends with a digit
    assert ends_with("hello world 123", "123") == True, "Failed on string ending with a digit"

    # Test case 17: String does not end with a digit
    assert ends_with("hello world 123", "124") == False, "Failed on string not ending with a digit"

    # Test case 18: String ends with mixed case suffix
    assert ends_with("hello world", "World") == False, "Failed on string ending with mixed case suffix"

    # Test case 19: String ends with mixed case suffix (case insensitive)
    assert ends_with("hello world", "World".lower()) == True, "Failed on string ending with mixed case suffix (case insensitive)"

    # Test case 20: String ends with non-English characters
    assert ends_with("héllo wörld", "wörld") == True, "Failed on string ending with non-English characters"

    # Test case 21: String does not end with non-English characters
    assert ends_with("héllo wörld", "world") == False, "Failed on string not ending with non-English characters"

    # Test case 22: String ends with punctuation
    assert ends_with("hello world!", "!") == True, "Failed on string ending with punctuation"

    # Test case 23: String does not end with punctuation
    assert ends_with("hello world", "!") == False, "Failed on string not ending with punctuation"

if __name__ == "__main__":
    pytest.main()