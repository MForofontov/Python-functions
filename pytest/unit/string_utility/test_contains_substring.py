import pytest
from strings_utility.contains_substring import contains_substring

def test_contains_substring() -> None:
    """
    Test the contains_substring function.

    This function tests the contains_substring function to ensure it correctly identifies
    whether a substring is present within a given string.
    """
    # Test case 1: Substring is present in the string
    assert contains_substring("hello world", "world") == True, "Failed on substring present"

    # Test case 2: Substring is not present in the string
    assert contains_substring("hello world", "there") == False, "Failed on substring not present"

    # Test case 3: Substring is the entire string
    assert contains_substring("hello", "hello") == True, "Failed on substring is the entire string"

    # Test case 4: Substring is an empty string
    assert contains_substring("hello", "") == True, "Failed on empty substring"

    # Test case 5: String is an empty string
    assert contains_substring("", "hello") == False, "Failed on empty string"

    # Test case 6: Both string and substring are empty
    assert contains_substring("", "") == True, "Failed on both string and substring empty"

    # Test case 7: Substring is at the beginning of the string
    assert contains_substring("hello world", "hello") == True, "Failed on substring at the beginning"

    # Test case 8: Substring is at the end of the string
    assert contains_substring("hello world", "world") == True, "Failed on substring at the end"

    # Test case 9: Substring is in the middle of the string
    assert contains_substring("hello world", "lo wo") == True, "Failed on substring in the middle"

    # Test case 10: Substring is a single character present in the string
    assert contains_substring("hello world", "o") == True, "Failed on single character present"

    # Test case 11: Substring is a single character not present in the string
    assert contains_substring("hello world", "x") == False, "Failed on single character not present"

    # Test case 12: Substring with special characters
    assert contains_substring("hello!@# world", "!@#") == True, "Failed on substring with special characters"

    # Test case 13: Substring with numbers
    assert contains_substring("hello123 world", "123") == True, "Failed on substring with numbers"

    # Test case 14: Substring with mixed case
    assert contains_substring("Hello World", "world") == False, "Failed on mixed case substring"

    # Test case 15: Substring with mixed case (case insensitive)
    assert contains_substring("Hello World", "World") == True, "Failed on mixed case substring (case insensitive)"

    # Test case 16: Substring with spaces
    assert contains_substring("hello world", " ") == True, "Failed on substring with spaces"

    # Test case 17: Substring with newline characters
    assert contains_substring("hello\nworld", "\n") == True, "Failed on substring with newline characters"

    # Test case 18: Substring with tab characters
    assert contains_substring("hello\tworld", "\t") == True, "Failed on substring with tab characters"

    # Test case 19: Substring with leading and trailing spaces
    assert contains_substring("  hello world  ", "hello") == True, "Failed on substring with leading and trailing spaces"

    # Test case 20: Substring with punctuation
    assert contains_substring("hello, world!", "world!") == True, "Failed on substring with punctuation"

    # Test case 21: Substring with non-English characters
    assert contains_substring("héllo wörld", "wörld") == True, "Failed on substring with non-English characters"

if __name__ == "__main__":
    pytest.main()