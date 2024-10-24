import pytest
from strings_utility.count_substring import count_substring

def test_count_substring() -> None:
    """
    Test the count_substring function.

    This function tests the count_substring function to ensure it correctly counts
    the number of non-overlapping occurrences of a substring in a given string.
    """
    # Test case 1: Substring occurs multiple times
    assert count_substring("hello world", "o") == 2, "Failed on multiple occurrences"

    # Test case 2: Substring occurs at the beginning
    assert count_substring("ababab", "ab") == 3, "Failed on substring at the beginning"

    # Test case 3: Substring occurs at the end
    assert count_substring("hello", "lo") == 1, "Failed on substring at the end"

    # Test case 4: Substring is the entire string
    assert count_substring("hello", "hello") == 1, "Failed on substring is the entire string"

    # Test case 5: Substring does not occur
    assert count_substring("hello", "world") == 0, "Failed on substring does not occur"

    # Test case 6: Empty substring
    assert count_substring("hello", "") == 6, "Failed on empty substring"

    # Test case 7: Empty string
    assert count_substring("", "hello") == 0, "Failed on empty string"

    # Test case 8: Both string and substring are empty
    assert count_substring("", "") == 1, "Failed on both string and substring empty"

    # Test case 9: Substring occurs with overlapping
    assert count_substring("aaaa", "aa") == 3, "Failed on overlapping occurrences"

    # Test case 10: Substring occurs with special characters
    assert count_substring("hello!@#hello", "hello") == 2, "Failed on special characters"

    # Test case 11: Substring occurs with mixed case
    assert count_substring("Hello hello", "hello") == 1, "Failed on mixed case"

    # Test case 12: Substring occurs with numbers
    assert count_substring("123123123", "123") == 3, "Failed on numbers"

    # Test case 13: Substring occurs with spaces
    assert count_substring("hello world hello", "hello") == 2, "Failed on spaces"

    # Test case 14: Substring occurs with newline characters
    assert count_substring("hello\nworld\nhello", "hello") == 2, "Failed on newline characters"

    # Test case 15: Substring occurs with tab characters
    assert count_substring("hello\tworld\thello", "hello") == 2, "Failed on tab characters"

    # Test case 16: Substring occurs with mixed whitespace characters
    assert count_substring("hello \t\nworld \t\nhello", "hello") == 2, "Failed on mixed whitespace characters"

    # Test case 17: Substring occurs with leading and trailing spaces
    assert count_substring("  hello world  hello  ", "hello") == 2, "Failed on leading and trailing spaces"

    # Test case 18: Substring occurs with punctuation
    assert count_substring("hello, world! hello.", "hello") == 2, "Failed on punctuation"

    # Test case 19: Substring occurs with non-English characters
    assert count_substring("héllo wörld héllo", "héllo") == 2, "Failed on non-English characters"

    # Test case 20: Substring occurs with overlapping and special characters
    assert count_substring("aa!aa!aa", "aa") == 3, "Failed on overlapping and special characters"

if __name__ == "__main__":
    pytest.main()