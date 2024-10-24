import pytest
from strings_utility.count_consonants import count_consonants

def test_count_consonants() -> None:
    """
    Test the count_consonants function.

    This function tests the count_consonants function to ensure it correctly counts
    the number of consonants in a given string.
    """
    # Test case 1: String with mixed case consonants and vowels
    assert count_consonants("hello") == 3, "Failed on mixed case consonants and vowels"

    # Test case 2: String with all consonants
    assert count_consonants("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 42, "Failed on all consonants"

    # Test case 3: String with all vowels
    assert count_consonants("aeiouAEIOU") == 0, "Failed on all vowels"

    # Test case 4: Empty string
    assert count_consonants("") == 0, "Failed on empty string"

    # Test case 5: String with numbers and special characters
    assert count_consonants("12345!@#$%") == 0, "Failed on string with numbers and special characters"

    # Test case 6: String with mixed consonants, vowels, numbers, and special characters
    assert count_consonants("h3ll0 w0rld!") == 7, "Failed on mixed consonants, vowels, numbers, and special characters"

    # Test case 7: String with uppercase consonants
    assert count_consonants("HELLO") == 3, "Failed on uppercase consonants"

    # Test case 8: String with mixed case consonants
    assert count_consonants("HeLLo WoRLd") == 7, "Failed on mixed case consonants"

    # Test case 9: String with spaces
    assert count_consonants("hello world") == 7, "Failed on string with spaces"

    # Test case 10: String with non-English characters
    assert count_consonants("héllo wörld") == 7, "Failed on string with non-English characters"

    # Test case 11: String with only consonants
    assert count_consonants("bcdfghjklmnpqrstvwxyz") == 21, "Failed on string with only consonants"

    # Test case 12: String with only uppercase consonants
    assert count_consonants("BCDFGHJKLMNPQRSTVWXYZ") == 21, "Failed on string with only uppercase consonants"

    # Test case 13: String with repeated consonants
    assert count_consonants("bbccddffgghhjjkkllmmnnppqqrrssttvvwwxxyyzz") == 42, "Failed on string with repeated consonants"

    # Test case 14: String with no consonants
    assert count_consonants("aeiou") == 0, "Failed on string with no consonants"

    # Test case 15: String with punctuation
    assert count_consonants("hello, world!") == 7, "Failed on string with punctuation"

    # Test case 16: String with newline characters
    assert count_consonants("hello\nworld") == 7, "Failed on string with newline characters"

    # Test case 17: String with tab characters
    assert count_consonants("hello\tworld") == 7, "Failed on string with tab characters"

    # Test case 18: String with mixed whitespace characters
    assert count_consonants("hello \t\nworld") == 7, "Failed on string with mixed whitespace characters"

    # Test case 19: String with leading and trailing spaces
    assert count_consonants("  hello world  ") == 7, "Failed on string with leading and trailing spaces"

if __name__ == "__main__":
    pytest.main()