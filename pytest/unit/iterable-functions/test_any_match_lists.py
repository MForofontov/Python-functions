import pytest
from iterable_functions.any_match_lists import any_match_lists

def test_any_match_lists_success() -> None:
    """
    Test the any_match_lists function with valid inputs where some elements match.
    """
    # Test case 1: Some elements match
    list1: list[int] = [1, 2, 6]
    list2: list[int] = [1, 2, 3, 4, 5]
    assert any_match_lists(list1, list2) == True

def test_any_match_lists_no_match() -> None:
    """
    Test the any_match_lists function with valid inputs where no elements match.
    """
    # Test case 2: No elements match
    list1: list[int] = [6, 7, 8]
    list2: list[int] = [1, 2, 3, 4, 5]
    assert any_match_lists(list1, list2) == False

def test_any_match_lists_empty_list1() -> None:
    """
    Test the any_match_lists function with an empty list1.
    """
    # Test case 3: Empty list1
    list1: list[int] = []
    list2: list[int] = [1, 2, 3, 4, 5]
    assert any_match_lists(list1, list2) == False

def test_any_match_lists_empty_list2() -> None:
    """
    Test the any_match_lists function with an empty list2.
    """
    # Test case 4: Empty list2
    list1: list[int] = [1, 2, 3]
    list2: list[int] = []
    assert any_match_lists(list1, list2) == False

def test_any_match_lists_two_empty_lists() -> None:
    """
    Test the any_match_lists function with two empty lists.
    """
    # Test case 5: Two empty lists
    list1: list[int] = []
    list2: list[int] = []
    assert any_match_lists(list1, list2) == False

def test_any_match_lists_type_error_list1() -> None:
    """
    Test the any_match_lists function with invalid type for list1.
    """
    # Test case 6: Invalid type for list1
    with pytest.raises(TypeError):
        any_match_lists("not a list", [1, 2, 3])

def test_any_match_lists_type_error_list2() -> None:
    """
    Test the any_match_lists function with invalid type for list2.
    """
    # Test case 7: Invalid type for list2
    with pytest.raises(TypeError):
        any_match_lists([1, 2, 3], "not a list")
