import pytest
from strings_utility.join_strings import join_strings

def test_join_strings() -> None:
    """
    Test the join_strings function.

    This function tests the join_strings function to ensure it correctly joins
    a list of strings using a specified delimiter.
    """
    # Test case 1: Join a list of strings with default delimiter (space)
    assert join_strings(["hello", "world"]) == "hello world", "Failed on default delimiter"

    # Test case 2: Join a list of strings with a custom delimiter
    assert join_strings(["hello", "world"], delimiter=",") == "hello,world", "Failed on custom delimiter"

    # Test case 3: Join a list of strings with an empty delimiter
    assert join_strings(["hello", "world"], delimiter="") == "helloworld", "Failed on empty delimiter"

    # Test case 4: Join a list of strings with a single string
    assert join_strings(["hello"]) == "hello", "Failed on single string"

    # Test case 5: Join an empty list of strings
    assert join_strings([]) == "", "Failed on empty list"

    # Test case 6: Join a list of strings with special characters
    assert join_strings(["hello", "world!"], delimiter=" ") == "hello world!", "Failed on special characters"

    # Test case 7: Join a list of strings with numbers
    assert join_strings(["123", "456"], delimiter="-") == "123-456", "Failed on numbers"

    # Test case 8: Join a list of strings with mixed case
    assert join_strings(["Hello", "World"], delimiter=" ") == "Hello World", "Failed on mixed case"

    # Test case 9: Join a list of strings with leading and trailing spaces
    assert join_strings(["  hello", "world  "], delimiter=" ") == "  hello world  ", "Failed on leading and trailing spaces"

    # Test case 10: Join a list of strings with newline characters
    assert join_strings(["hello", "world"], delimiter="\n") == "hello\nworld", "Failed on newline characters"

    # Test case 11: Join a list of strings with tab characters
    assert join_strings(["hello", "world"], delimiter="\t") == "hello\tworld", "Failed on tab characters"

    # Test case 12: Join a list of strings with mixed whitespace characters
    assert join_strings(["hello", "world"], delimiter=" \t\n") == "hello \t\nworld", "Failed on mixed whitespace characters"

    # Test case 13: Join a list of strings with non-English characters
    assert join_strings(["héllo", "wörld"], delimiter=" ") == "héllo wörld", "Failed on non-English characters"

    # Test case 14: Join a list of strings with punctuation
    assert join_strings(["hello,", "world!"], delimiter=" ") == "hello, world!", "Failed on punctuation"

    # Test case 15: Join a list of strings with mixed alphanumeric characters
    assert join_strings(["abc123", "456def"], delimiter=" ") == "abc123 456def", "Failed on mixed alphanumeric characters"

    # Test case 16: Join a list of strings with leading and trailing delimiters
    assert join_strings(["hello", "world"], delimiter=" ") == "hello world", "Failed on leading and trailing delimiters"

    # Test case 17: Join a list of strings with multiple delimiters
    assert join_strings(["hello", "world"], delimiter="---") == "hello---world", "Failed on multiple delimiters"

if __name__ == "__main__":
    pytest.main()