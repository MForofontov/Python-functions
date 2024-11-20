import pytest
from typing import Any
from iterable_functions.identify_dict_structure import identify_dict_structure

def test_identify_dict_structure_success() -> None:
    """
    Test the identify_dict_structure function with valid inputs.
    """
    # Test case 1: Valid inputs
    list_of_dicts: list[dict[str, Any]] = [
        {"a": 1, "b": "string"},
        {"b": "another string", "c": [1, 2, 3]},
        {"d": {"nested": "dict", "e": {"nested_again": "value"}}}
    ]
    expected_output: dict[str, None] = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "d.nested": None,
        "d.e": None,
        "d.e.nested_again": None
    }
    assert identify_dict_structure(list_of_dicts) == expected_output

def test_identify_dict_structure_empty_list() -> None:
    """
    Test the identify_dict_structure function with an empty list.
    """
    # Test case 2: Empty list
    list_of_dicts: list[dict[str, Any]] = []
    expected_output: dict[str, None] = {}
    assert identify_dict_structure(list_of_dicts) == expected_output

def test_identify_dict_structure_single_dict() -> None:
    """
    Test the identify_dict_structure function with a single dictionary.
    """
    # Test case 3: Single dictionary
    list_of_dicts: list[dict[str, Any]] = [{"a": 1, "b": "string"}]
    expected_output: dict[str, None] = {"a": None, "b": None}
    assert identify_dict_structure(list_of_dicts) == expected_output

def test_identify_dict_structure_nested_dicts() -> None:
    """
    Test the identify_dict_structure function with nested dictionaries.
    """
    # Test case 4: Nested dictionaries
    list_of_dicts: list[dict[str, Any]] = [
        {"a": 1, "b": {"nested": "dict"}},
        {"c": {"nested_again": {"deeply_nested": "value"}}}
    ]
    expected_output: dict[str, None] = {
        "a": None,
        "b": None,
        "b.nested": None,
        "c": None,
        "c.nested_again": None,
        "c.nested_again.deeply_nested": None
    }
    assert identify_dict_structure(list_of_dicts) == expected_output

def test_identify_dict_structure_type_error_list_of_dicts() -> None:
    """
    Test the identify_dict_structure function with invalid type for list_of_dicts.
    """
    # Test case 5: Invalid type for list_of_dicts
    with pytest.raises(TypeError):
        identify_dict_structure("not a list")

def test_identify_dict_structure_type_error_elements() -> None:
    """
    Test the identify_dict_structure function with invalid elements in list_of_dicts.
    """
    # Test case 6: Invalid elements in list_of_dicts
    with pytest.raises(TypeError):
        identify_dict_structure([{"a": 1}, "not a dict"])
