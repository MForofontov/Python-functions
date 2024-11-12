import pytest
from iterable_functions.check_if_all_elements_are_duplicates import check_if_all_elements_are_duplicates

def test_check_if_all_elements_are_duplicates_all_duplicates() -> None:
    """
    Test the check_if_all_elements_are_duplicates function with all elements being duplicates.
    """
    # Test case 1: All elements are duplicates
    input_list: list[int] = [1, 1, 2, 2, 3, 3]
    assert check_if_all_elements_are_duplicates(input_list) == True

def test_check_if_all_elements_are_duplicates_no_duplicates() -> None:
    """
    Test the check_if_all_elements_are_duplicates function with no elements being duplicates.
    """
    # Test case 2: No elements are duplicates
    input_list: list[int] = [1, 2, 3, 4, 5]
    assert check_if_all_elements_are_duplicates(input_list) == False

def test_check_if_all_elements_are_duplicates_some_duplicates() -> None:
    """
    Test the check_if_all_elements_are_duplicates function with some elements being duplicates.
    """
    # Test case 3: Some elements are duplicates
    input_list: list[int] = [1, 1, 2, 3, 4, 4]
    assert check_if_all_elements_are_duplicates(input_list) == False

def test_check_if_all_elements_are_duplicates_empty_list() -> None:
    """
    Test the check_if_all_elements_are_duplicates function with an empty list.
    """
    # Test case 4: Empty list
    input_list: list[int] = []
    assert check_if_all_elements_are_duplicates(input_list) == False

def test_check_if_all_elements_are_duplicates_type_error() -> None:
    """
    Test the check_if_all_elements_are_duplicates function with invalid type for input_list.
    """
    # Test case 5: Invalid type for input_list
    with pytest.raises(TypeError):
        check_if_all_elements_are_duplicates("not a list")
