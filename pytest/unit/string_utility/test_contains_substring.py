import pytest
from strings_utility.contains_substring import contains_substring

def test_contains_substring():
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

if __name__ == "__main__":
    pytest.main()