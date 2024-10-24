import pytest
from strings_utility.find_substring import find_substring

def test_find_substring() -> None:
    """
    Test the find_substring function.

    This function tests the find_substring function to ensure it correctly finds
    the first occurrence of a substring in a string.
    """
    # Test case 1: Substring is present in the string
    assert find_substring("hello world", "world") == 6, "Failed on substring present"

    # Test case 2: Substring is not present in the string
    assert find_substring("hello world", "there") == -1, "Failed on substring not present"

    # Test case 3: Substring is the entire string
    assert find_substring("hello", "hello") == 0, "Failed on substring is the entire string"

    # Test case 4: Substring is an empty string
    assert find_substring("hello", "") == 0, "Failed on empty substring"

    # Test case 5: String is an empty string
    assert find_substring("", "hello") == -1, "Failed on empty string"

    # Test case 6: Both string and substring are empty
    assert find_substring("", "") == 0, "Failed on both string and substring empty"

    # Test case 7: Substring is at the beginning of the string
    assert find_substring("hello world", "hello") == 0, "Failed on substring at the beginning"

    # Test case 8: Substring is at the end of the string
    assert find_substring("hello world", "world") == 6, "Failed on substring at the end"

    # Test case 9: Substring is in the middle of the string
    assert find_substring("hello world", "lo wo") == 3, "Failed on substring in the middle"

    # Test case 10: Substring is a single character present in the string
    assert find_substring("hello world", "o") == 4, "Failed on single character present"

    # Test case 11: Substring is a single character not present in the string
    assert find_substring("hello world", "x") == -1, "Failed on single character not present"

    # Test case 12: Substring with special characters
    assert find_substring("hello!@# world", "!@#") == 5, "Failed on substring with special characters"

    # Test case 13: Substring with numbers
    assert find_substring("hello123 world", "123") == 5, "Failed on substring with numbers"

    # Test case 14: Substring with mixed case
    assert find_substring("Hello World", "world") == -1, "Failed on mixed case substring"

    # Test case 15: Substring with mixed case (case sensitive)
    assert find_substring("Hello World", "World") == 6, "Failed on mixed case substring (case sensitive)"

    # Test case 16: Substring with spaces
    assert find_substring("hello world", " ") == 5, "Failed on substring with spaces"

    # Test case 17: Substring with newline characters
    assert find_substring("hello\nworld", "\n") == 5, "Failed on substring with newline characters"

    # Test case 18: Substring with tab characters
    assert find_substring("hello\tworld", "\t") == 5, "Failed on substring with tab characters"

    # Test case 19: Substring with leading and trailing spaces
    assert find_substring("  hello world  ", "hello") == 2, "Failed on substring with leading and trailing spaces"

    # Test case 20: Substring with punctuation
    assert find_substring("hello, world!", "world!") == 7, "Failed on substring with punctuation"

    # Test case 21: Substring with non-English characters
    assert find_substring("héllo wörld", "wörld") == 6, "Failed on substring with non-English characters"

if __name__ == "__main__":
    pytest.main()