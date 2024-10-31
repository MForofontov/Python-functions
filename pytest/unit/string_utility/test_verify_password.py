import pytest
from strings_utility.verify_password import verify_password

def test_verify_password_valid() -> None:
    """
    Test the verify_password function with a valid password.
    """
    # Test case 1: Valid password
    assert verify_password("Password123!") == True, "Failed on valid password"

def test_verify_password_too_short() -> None:
    """
    Test the verify_password function with a password that is too short.
    """
    # Test case 2: Password too short
    assert verify_password("Pass1!") == False, "Failed on password too short"

def test_verify_password_no_uppercase() -> None:
    """
    Test the verify_password function with a password that has no uppercase characters.
    """
    # Test case 3: No uppercase characters
    assert verify_password("password123!") == False, "Failed on no uppercase characters"

def test_verify_password_no_lowercase() -> None:
    """
    Test the verify_password function with a password that has no lowercase characters.
    """
    # Test case 4: No lowercase characters
    assert verify_password("PASSWORD123!") == False, "Failed on no lowercase characters"

def test_verify_password_no_digit() -> None:
    """
    Test the verify_password function with a password that has no numerical digits.
    """
    # Test case 5: No numerical digits
    assert verify_password("Password!!!") == False, "Failed on no numerical digits"

def test_verify_password_no_special_character() -> None:
    """
    Test the verify_password function with a password that has no special characters.
    """
    # Test case 6: No special characters
    assert verify_password("Password123") == False, "Failed on no special characters"

def test_verify_password_only_special_characters() -> None:
    """
    Test the verify_password function with a password that has only special characters.
    """
    # Test case 7: Only special characters
    assert verify_password("!@#$%^&*") == False, "Failed on only special characters"

def test_verify_password_only_digits() -> None:
    """
    Test the verify_password function with a password that has only digits.
    """
    # Test case 8: Only digits
    assert verify_password("12345678") == False, "Failed on only digits"

def test_verify_password_only_uppercase() -> None:
    """
    Test the verify_password function with a password that has only uppercase characters.
    """
    # Test case 9: Only uppercase characters
    assert verify_password("PASSWORD") == False, "Failed on only uppercase characters"

def test_verify_password_only_lowercase() -> None:
    """
    Test the verify_password function with a password that has only lowercase characters.
    """
    # Test case 10: Only lowercase characters
    assert verify_password("password") == False, "Failed on only lowercase characters"

def test_verify_password_empty_string() -> None:
    """
    Test the verify_password function with an empty string.
    """
    # Test case 11: Empty string
    assert verify_password("") == False, "Failed on empty string"

def test_verify_password_non_english_characters() -> None:
    """
    Test the verify_password function with a password that contains non-English characters.
    """
    # Test case 12: Non-English characters
    assert verify_password("Pässwörd123!") == True, "Failed on non-English characters"

def test_verify_password_mixed_whitespace() -> None:
    """
    Test the verify_password function with a password that contains mixed whitespace characters.
    """
    # Test case 13: Mixed whitespace characters
    assert verify_password("Pass word123!") == True, "Failed on mixed whitespace characters"

def test_verify_password_invalid_type() -> None:
    """
    Test the verify_password function with an invalid type.
    """
    # Test case 14: Invalid type
    with pytest.raises(TypeError):
        verify_password(12345678)

if __name__ == "__main__":
    pytest.main()
