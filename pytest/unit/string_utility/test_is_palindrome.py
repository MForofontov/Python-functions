import pytest
from strings_utility.is_palindrome import is_palindrome

def test_is_palindrome() -> None:
    """
    Test the is_palindrome function.

    This function tests the is_palindrome function to ensure it correctly identifies
    whether a string is a palindrome.
    """
    # Test case 1: Palindrome with odd length
    assert is_palindrome("racecar") == True, "Failed on palindrome with odd length"

    # Test case 2: Palindrome with even length
    assert is_palindrome("abba") == True, "Failed on palindrome with even length"

    # Test case 3: Non-palindrome with odd length
    assert is_palindrome("hello") == False, "Failed on non-palindrome with odd length"

    # Test case 4: Non-palindrome with even length
    assert is_palindrome("abcd") == False, "Failed on non-palindrome with even length"

    # Test case 5: Single character string
    assert is_palindrome("a") == True, "Failed on single character string"

    # Test case 6: Empty string
    assert is_palindrome("") == True, "Failed on empty string"

    # Test case 7: Palindrome with mixed case
    assert is_palindrome("RaceCar") == False, "Failed on palindrome with mixed case"

    # Test case 8: Palindrome with spaces
    assert is_palindrome("a man a plan a canal panama") == False, "Failed on palindrome with spaces"

    # Test case 9: Palindrome with punctuation
    assert is_palindrome("A man, a plan, a canal, Panama!") == False, "Failed on palindrome with punctuation"

    # Test case 10: Palindrome with numbers
    assert is_palindrome("12321") == True, "Failed on palindrome with numbers"

    # Test case 11: Non-palindrome with numbers
    assert is_palindrome("12345") == False, "Failed on non-palindrome with numbers"

    # Test case 12: Palindrome with special characters
    assert is_palindrome("@#@") == True, "Failed on palindrome with special characters"

    # Test case 13: Non-palindrome with special characters
    assert is_palindrome("@#a") == False, "Failed on non-palindrome with special characters"

    # Test case 14: Palindrome with mixed alphanumeric characters
    assert is_palindrome("A1B2B1A") == True, "Failed on palindrome with mixed alphanumeric characters"

    # Test case 15: Non-palindrome with mixed alphanumeric characters
    assert is_palindrome("A1B2C3") == False, "Failed on non-palindrome with mixed alphanumeric characters"

    # Test case 16: Palindrome with leading and trailing spaces
    assert is_palindrome(" racecar ") == False, "Failed on palindrome with leading and trailing spaces"

    # Test case 17: Palindrome with newline characters
    assert is_palindrome("race\ncar") == False, "Failed on palindrome with newline characters"

    # Test case 18: Palindrome with tab characters
    assert is_palindrome("race\tcar") == False, "Failed on palindrome with tab characters"

    # Test case 19: Palindrome with mixed whitespace characters
    assert is_palindrome("race \t\ncar") == False, "Failed on palindrome with mixed whitespace characters"

if __name__ == "__main__":
    pytest.main()