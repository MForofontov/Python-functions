import pytest
from iterable_functions.all_match_lists import all_match_lists

def test_all_match_lists_success() -> None:
    """
    Test the all_match_lists function with valid inputs where all elements match.
    """
    # Test case 1: All elements match
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [1, 2, 3, 4, 5]
    assert all_match_lists(list1, list2) == True

def test_all_match_lists_partial_match() -> None:
    """
    Test the all_match_lists function with valid inputs where not all elements match.
    """
    # Test case 2: Not all elements match
    list1: list[int] = [1, 2, 6]
    list2: list[int] = [1, 2, 3, 4, 5]
    assert all_match_lists(list1, list2) == False

def test_all_match_lists_empty_list1() -> None:
    """
    Test the all_match_lists function with an empty list1.
    """
    # Test case 3: Empty list1
    list1: list[int] = []
    list2: list[int] = [1, 2, 3, 4, 5]
    assert all_match_lists(list1, list2) == True

def test_all_match_lists_empty_list2() -> None:
    """
    Test the all_match_lists function with an empty list2.
    """
    # Test case 4: Empty list2
    list1: list[int] = [1, 2, 3]
    list2: list[int] = []
    assert all_match_lists(list1, list2) == False

def test_all_match_lists_type_error_list1() -> None:
    """
    Test the all_match_lists function with invalid type for list1.
    """
    # Test case 5: Invalid type for list1
    with pytest.raises(TypeError):
        all_match_lists("not a list", [1, 2, 3])

def test_all_match_lists_type_error_list2() -> None:
    """
    Test the all_match_lists function with invalid type for list2.
    """
    # Test case 6: Invalid type for list2
    with pytest.raises(TypeError):
        all_match_lists([1, 2, 3], "not a list")
