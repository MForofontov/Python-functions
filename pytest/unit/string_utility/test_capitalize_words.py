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

if __name__ == "__main__":
    pytest.main()