from collections import Counter

def is_anagram(string_1: str, string_2: str) -> bool:
    """
    Check if two strings are anagrams.

    Parameters
    ----------
    str1 : str
        The first string.
    str2 : str
        The second string.

    Returns
    -------
    bool
        True if the strings are anagrams, False otherwise.

    Raises
    ------
    TypeError
        If either of the inputs is not a string.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")

    # Remove any whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Use Counter to compare the frequency of characters in both strings
    return Counter(str1) == Counter(str2)