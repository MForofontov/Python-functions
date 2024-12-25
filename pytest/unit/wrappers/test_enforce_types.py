import pytest
import logging
from decorators.enforce_types import enforce_types

# Configure test_logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

# Example function to be decorated
@enforce_types(logger=test_logger)
def sample_function(a: int, b: str) -> str:
    return f"{a} - {b}"

def test_valid_types():
    """
    Test case 1: Valid types for arguments and return value
    """
    result = sample_function(1, "test")
    assert result == "1 - test"

def test_valid_types_with_logger(caplog):
    """
    Test case 2: Valid types for arguments and return value, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_valid_with_logger(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.INFO):
        result = sample_function_valid_with_logger(1, "test")
    assert result == "1 - test"
    assert "Argument 'a' must be of type int" not in caplog.text
    assert "Return value must be of type int" not in caplog.text

def test_invalid_argument_type():
    """
    Test case 3: Invalid type for argument, no logger provided
    """
    @enforce_types()
    def sample_function_invalid_arg(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with pytest.raises(TypeError, match="Argument 'a' must be of type int"):
        sample_function_invalid_arg("invalid", "test")

def test_invalid_return_type():
    """
    Test case 4: Invalid type for return value, no logger provided
    """
    @enforce_types()
    def sample_function_invalid_return(a: int, b: str) -> int:
        return f"{a} - {b}"
    
    with pytest.raises(TypeError, match="Return value must be of type int"):
        sample_function_invalid_return(1, "test")

def test_invalid_argument_type_with_logger(caplog):
    """
    Test case 5: Invalid type for argument, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_invalid_arg_with_logger(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match="Argument 'a' must be of type int"):
            sample_function_invalid_arg_with_logger("invalid", "test")
    assert "Argument 'a' must be of type int" in caplog.text

def test_invalid_return_type_with_logger(caplog):
    """
    Test case 6: Invalid type for return value, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_invalid_return_with_logger(a: int, b: str) -> int:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match="Return value must be of type int"):
            sample_function_invalid_return_with_logger(1, "test")
    assert "Return value must be of type int" in caplog.text

def test_invalid_argument_type_with_kwargs():
    """
    Test case 7: Invalid type for argument with kwargs, no logger provided
    """
    @enforce_types()
    def sample_function_invalid_arg_kwargs(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with pytest.raises(TypeError, match="Argument 'a' must be of type int"):
        sample_function_invalid_arg_kwargs(a="invalid", b="test")

def test_invalid_argument_type_with_kwargs_and_logger(caplog):
    """
    Test case 8: Invalid type for argument with kwargs, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_invalid_arg_kwargs_with_logger(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.ERROR):
        sample_function_invalid_arg_kwargs_with_logger(a="invalid", b="test")
    assert "Argument 'a' must be of type int" in caplog.text

def test_valid_types_with_kwargs():
    """
    Test case 9: Valid types for arguments with kwargs
    """
    @enforce_types()
    def sample_function_valid_kwargs(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    result = sample_function_valid_kwargs(a=1, b="test")
    assert result == "1 - test"

def test_valid_types_with_kwargs_and_logger(caplog):
    """
    Test case 10: Valid types for arguments with kwargs, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_valid_kwargs_with_logger(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.INFO):
        result = sample_function_valid_kwargs_with_logger(a=1, b="test")
    assert result == "1 - test"
    assert "Argument 'a' must be of type int" not in caplog.text
    assert "Return value must be of type int" not in caplog.text

def test_invalid_logger():
    """
    Test case 11: Invalid logger
    """
    with pytest.raises(TypeError, match="logger must be an instance of logging.Logger or None"):
        @enforce_types(logger="invalid_logger")
        def sample_function_invalid_logger(a: int, b: str) -> str:
            return f"{a} - {b}"
