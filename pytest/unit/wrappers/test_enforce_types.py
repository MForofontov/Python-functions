import pytest
import logging
from decorators.enforce_types import enforce_types

# Configure test_logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

@enforce_types(logger=test_logger)
def sample_function(a: int, b: str) -> str:
    return f"a: {a}, b: {b}"

def test_correct_types():
    """
    Test case 1: Correct types
    """
    # Test case 1: Correct types
    result = sample_function(1, "test")
    assert result == "a: 1, b: test"

def test_optional_arguments():
    """
    Test case 2: Optional arguments
    """
    # Test case 2: Optional arguments
    @enforce_types()
    def sample_function_optional(a: int, b: str = "default") -> str:
        return f"a: {a}, b: {b}"
    
    result = sample_function_optional(1)
    assert result == "a: 1, b: default"
    result = sample_function_optional(1, "test")
    assert result == "a: 1, b: test"

def test_incorrect_positional_type(caplog):
    """
    Test case 3: Incorrect positional argument type
    """
    # Test case 3: Incorrect positional argument type
    with caplog.at_level(logging.ERROR):
        sample_function("wrong type", "test")
    assert "Expected <class 'int'> for argument 'a', got <class 'str'>" in caplog.text

def test_incorrect_keyword_type(caplog):
    """
    Test case 4: Incorrect keyword argument type
    """
    # Test case 4: Incorrect keyword argument type
    with caplog.at_level(logging.ERROR):
        sample_function(a=1, b=2)
    assert "Expected <class 'str'> for argument 'b', got <class 'int'>" in caplog.text

def test_no_logger():
    """
    Test case 5: No logger provided
    """
    # Test case 5: No logger provided
    @enforce_types()
    def sample_function_no_logger(a: int, b: str) -> str:
        return f"a: {a}, b: {b}"
    
    with pytest.raises(TypeError):
        sample_function_no_logger("wrong type", "test")

def test_return_type(caplog):
    """
    Test case 6: Return type
    """
    # Test case 6: Return type
    @enforce_types(logger=test_logger)
    def sample_function_return(a: int, b: str) -> int:
        return f"a: {a}, b: {b}"
    
    with caplog.at_level(logging.ERROR):
        sample_function_return(1, "test")
    assert "Expected return type <class 'int'>, got <class 'str'>" in caplog.text

def test_union_type(caplog):
    """
    Test case 7: Union type
    """
    # Test case 7: Union type
    from typing import Union

    @enforce_types(logger=test_logger)
    def sample_function_union(a: Union[int, str]) -> str:
        return f"a: {a}"
    
    result = sample_function_union(1)
    assert result == "a: 1"
    result = sample_function_union("test")
    assert result == "a: test"
    
    with caplog.at_level(logging.ERROR):
        sample_function_union(1.0)
    assert "Expected typing.Union[int, str] for argument 'a', got <class 'float'>" in caplog.text

def test_list_type(caplog):
    """
    Test case 8: List type
    """
    # Test case 8: List type
    from typing import List

    @enforce_types(logger=test_logger)
    def sample_function_list(a: List[int]) -> str:
        return f"a: {a}"
    
    result = sample_function_list([1, 2, 3])
    assert result == "a: [1, 2, 3]"
    
    with caplog.at_level(logging.ERROR):
        sample_function_list(["test"])
    assert "Expected <class 'int'> for argument 'a', got <class 'str'>" in caplog.text

def test_dict_type(caplog):
    """
    Test case 9: Dict type
    """
    # Test case 9: Dict type
    from typing import Dict

    @enforce_types(logger=test_logger)
    def sample_function_dict(a: Dict[str, int]) -> str:
        return f"a: {a}"
    
    result = sample_function_dict({"key": 1})
    assert result == "a: {'key': 1}"
    
    with caplog.at_level(logging.ERROR):
        sample_function_dict({1: "value"})
    assert "Expected <class 'str'> for argument 'a', got <class 'int'>" in caplog.text
