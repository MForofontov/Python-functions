import pytest
from strings_utility.expand_tabs import expand_tabs

def test_expand_tabs_default_tabsize() -> None:
    """
    Test the expand_tabs function with the default tab size (8 spaces).
    """
    # Test case 1: Default tab size (8 spaces)
    assert expand_tabs("hello\tworld") == "hello       world", "Failed on default tab size"

def test_expand_tabs_custom_tabsize() -> None:
    """
    Test the expand_tabs function with a custom tab size (4 spaces).
    """
    # Test case 2: Custom tab size (4 spaces)
    assert expand_tabs("hello\tworld", tabsize=4) == "hello    world", "Failed on custom tab size"

def test_expand_tabs_multiple_tabs_default_tabsize() -> None:
    """
    Test the expand_tabs function with multiple tabs and the default tab size.
    """
    # Test case 3: Multiple tabs with default tab size
    assert expand_tabs("hello\tworld\t!") == "hello       world       !", "Failed on multiple tabs with default tab size"

def test_expand_tabs_multiple_tabs_custom_tabsize() -> None:
    """
    Test the expand_tabs function with multiple tabs and a custom tab size.
    """
    # Test case 4: Multiple tabs with custom tab size
    assert expand_tabs("hello\tworld\t!", tabsize=4) == "hello    world    !", "Failed on multiple tabs with custom tab size"

def test_expand_tabs_no_tabs() -> None:
    """
    Test the expand_tabs function with a string that contains no tabs.
    """
    # Test case 5: No tabs in the string
    assert expand_tabs("helloworld") == "helloworld", "Failed on no tabs in the string"

def test_expand_tabs_empty_string() -> None:
    """
    Test the expand_tabs function with an empty string.
    """
    # Test case 6: Empty string
    assert expand_tabs("") == "", "Failed on empty string"

def test_expand_tabs_only_tabs() -> None:
    """
    Test the expand_tabs function with a string that contains only tabs.
    """
    # Test case 7: String with only tabs
    assert expand_tabs("\t\t\t") == "                        ", "Failed on string with only tabs"

def test_expand_tabs_tabs_and_spaces() -> None:
    """
    Test the expand_tabs function with a string that contains both tabs and spaces.
    """
    # Test case 8: String with tabs and spaces
    assert expand_tabs("hello\t world") == "hello        world", "Failed on string with tabs and spaces"

def test_expand_tabs_tabs_at_beginning() -> None:
    """
    Test the expand_tabs function with a string that has tabs at the beginning.
    """
    # Test case 9: String with tabs at the beginning
    assert expand_tabs("\thello") == "        hello", "Failed on string with tabs at the beginning"

def test_expand_tabs_tabs_at_end() -> None:
    """
    Test the expand_tabs function with a string that has tabs at the end.
    """
    # Test case 10: String with tabs at the end
    assert expand_tabs("hello\t") == "hello       ", "Failed on string with tabs at the end"

def test_expand_tabs_mixed_tabs_newlines() -> None:
    """
    Test the expand_tabs function with a string that contains both tabs and newlines.
    """
    # Test case 11: String with mixed tabs and newlines
    assert expand_tabs("hello\tworld\nhello\tworld") == "hello       world\nhello       world", "Failed on string with mixed tabs and newlines"

def test_expand_tabs_custom_tabsize_mixed_tabs_newlines() -> None:
    """
    Test the expand_tabs function with a string that contains both tabs and newlines, and a custom tab size.
    """
    # Test case 12: String with custom tab size and mixed tabs and newlines
    assert expand_tabs("hello\tworld\nhello\tworld", tabsize=4) == "hello    world\nhello    world", "Failed on string with custom tab size and mixed tabs and newlines"

def test_expand_tabs_tabs_special_characters() -> None:
    """
    Test the expand_tabs function with a string that contains tabs and special characters.
    """
    # Test case 13: String with tabs and special characters
    assert expand_tabs("hello\tworld!@#") == "hello       world!@#", "Failed on string with tabs and special characters"

def test_expand_tabs_tabs_numbers() -> None:
    """
    Test the expand_tabs function with a string that contains tabs and numbers.
    """
    # Test case 14: String with tabs and numbers
    assert expand_tabs("hello\t12345") == "hello       12345", "Failed on string with tabs and numbers"

def test_expand_tabs_tabs_mixed_case() -> None:
    """
    Test the expand_tabs function with a string that contains tabs and mixed case letters.
    """
    # Test case 15: String with tabs and mixed case letters
    assert expand_tabs("HeLLo\tWoRLd") == "HeLLo       WoRLd", "Failed on string with tabs and mixed case letters"

def test_expand_tabs_tabs_non_english_characters() -> None:
    """
    Test the expand_tabs function with a string that contains tabs and non-English characters.
    """
    # Test case 16: String with tabs and non-English characters
    assert expand_tabs("héllo\twörld") == "héllo       wörld", "Failed on string with tabs and non-English characters"

def test_expand_tabs_tabs_leading_spaces() -> None:
    """
    Test the expand_tabs function with a string that contains tabs and leading spaces.
    """
    # Test case 17: String with tabs and leading spaces
    assert expand_tabs("    \thello") == "            hello", "Failed on string with tabs and leading spaces"

def test_expand_tabs_tabs_trailing_spaces() -> None:
    """
    Test the expand_tabs function with a string that contains tabs and trailing spaces.
    """
    # Test case 18: String with tabs and trailing spaces
    assert expand_tabs("hello\t    ") == "hello           ", "Failed on string with tabs and trailing spaces"

if __name__ == "__main__":
    pytest.main()
