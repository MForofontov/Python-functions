import pytest
from typing import Any
from iterable_functions.get_shared_elements import get_shared_elements

def test_get_shared_elements_success() -> None:
    """
    Test the get_shared_elements function with valid inputs.
    """
    # Test case 1: Valid inputs
    dict_: dict[str, list[int]] = {
        "list1": [1, 2, 3],
        "list2": [2, 3, 4],
        "list3": [3, 4, 5]
    }
    expected_output: list[int] = [2, 3, 4]
    assert get_shared_elements(dict_) == expected_output

def test_get_shared_elements_no_shared_elements() -> None:
    """
    Test the get_shared_elements function with no shared elements.
    """
    # Test case 2: No shared elements
    dict_: dict[str, list[int]] = {
        "list1": [1, 2],
        "list2": [3, 4],
        "list3": [5, 6]
    }
    expected_output: list[int] = []
    assert get_shared_elements(dict_) == expected_output

def test_get_shared_elements_empty_dict() -> None:
    """
    Test the get_shared_elements function with an empty dictionary.
    """
    # Test case 3: Empty dictionary
    dict_: dict[str, list[int]] = {}
    expected_output: list[int] = []
    assert get_shared_elements(dict_) == expected_output

def test_get_shared_elements_empty_lists() -> None:
    """
    Test the get_shared_elements function with empty lists.
    """
    # Test case 4: Empty lists
    dict_: dict[str, list[int]] = {
        "list1": [],
        "list2": [],
        "list3": []
    }
    expected_output: list[int] = []
    assert get_shared_elements(dict_) == expected_output

def test_get_shared_elements_strings() -> None:
    """
    Test the get_shared_elements function with lists of strings.
    """
    # Test case 5: Lists of strings
    dict_: dict[str, list[str]] = {
        "list1": ["apple", "banana"],
        "list2": ["banana", "cherry"],
        "list3": ["banana", "date"]
    }
    expected_output: list[str] = ["banana"]
    assert get_shared_elements(dict_) == expected_output

def test_get_shared_elements_mixed_types() -> None:
    """
    Test the get_shared_elements function with lists of mixed types.
    """
    # Test case 6: Lists of mixed types
    dict_: dict[str, list[Any]] = {
        "list1": [1, "banana"],
        "list2": [3.14, "banana"],
        "list3": [True, "banana"]
    }
    expected_output: list[Any] = ["banana"]
    assert get_shared_elements(dict_) == expected_output

def test_get_shared_elements_type_error_dict() -> None:
    """
    Test the get_shared_elements function with invalid type for dict_.
    """
    # Test case 7: Invalid type for dict_
    with pytest.raises(TypeError):
        get_shared_elements("not a dictionary")

def test_get_shared_elements_type_error_elements() -> None:
    """
    Test the get_shared_elements function with invalid elements in dict_.
    """
    # Test case 8: Invalid elements in dict_
    with pytest.raises(TypeError):
        get_shared_elements({"list1": [1, 2], "list2": "not a list"})
