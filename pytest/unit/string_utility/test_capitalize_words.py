import pytest
from strings_utility.capitalize_words import capitalize_words

def test_capitalize_words() -> None:
    """
    Test the capitalize_words function.

    This function tests the capitalize_words function to ensure it correctly capitalizes
    the first letter of each word in a string.
    """
    # Test case 1: Single word
    assert capitalize_words("hello") == "Hello", "Failed on single word"

    # Test case 2: Multiple words
    assert capitalize_words("hello world") == "Hello World", "Failed on multiple words"

    # Test case 3: Mixed case words
    assert capitalize_words("python programming") == "Python Programming", "Failed on mixed case words"

    # Test case 4: All uppercase words
    assert capitalize_words("CAPITALIZE EACH WORD") == "Capitalize Each Word", "Failed on all uppercase words"

    # Test case 5: All lowercase words
    assert capitalize_words("capitalize each word") == "Capitalize Each Word", "Failed on all lowercase words"

    # Test case 6: Words with punctuation
    assert capitalize_words("hello, world!") == "Hello, World!", "Failed on words with punctuation"

    # Test case 7: Words with numbers
    assert capitalize_words("hello world 123") == "Hello World 123", "Failed on words with numbers"

    # Test case 8: Empty string
    assert capitalize_words("") == "", "Failed on empty string"

    # Test case 9: String with only spaces
    assert capitalize_words("   ") == "   ", "Failed on string with only spaces"

    # Test case 10: String with leading and trailing spaces
    assert capitalize_words("  hello world  ") == "  Hello World  ", "Failed on string with leading and trailing spaces"

    # Test case 11: String with mixed whitespace characters
    assert capitalize_words("hello\tworld\npython") == "Hello\tWorld\nPython", "Failed on string with mixed whitespace characters"

    # Test case 12: String with special characters
    assert capitalize_words("hello!@# world") == "Hello!@# World", "Failed on string with special characters"

    # Test case 13: String with newline characters
    assert capitalize_words("hello\nworld") == "Hello\nWorld", "Failed on string with newline characters"

    # Test case 14: String with tab characters
    assert capitalize_words("hello\tworld") == "Hello\tWorld", "Failed on string with tab characters"

    # Test case 15: String with mixed case and special characters
    assert capitalize_words("hello!@# WORLD") == "Hello!@# WORLD", "Failed on string with mixed case and special characters"

    # Test case 16: String with leading and trailing special characters
    assert capitalize_words("!@#hello world!@#") == "!@#Hello World!@#", "Failed on string with leading and trailing special characters"

    # Test case 17: String with mixed case and numbers
    assert capitalize_words("hello123 world456") == "Hello123 World456", "Failed on string with mixed case and numbers"

    # Test case 18: String with leading and trailing numbers
    assert capitalize_words("123hello world456") == "123Hello World456", "Failed on string with leading and trailing numbers"

    # Test case 19: String with mixed case and punctuation
    assert capitalize_words("hello, world!") == "Hello, World!", "Failed on string with mixed case and punctuation"

    # Test case 20: String with leading and trailing punctuation
    assert capitalize_words(",hello world!") == ",Hello World!", "Failed on string with leading and trailing punctuation"

if __name__ == "__main__":
    pytest.main()