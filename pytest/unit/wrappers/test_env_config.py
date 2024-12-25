import os
import pytest
import logging
from env_config import env_config

# Configure test_logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

# Example function to be decorated
@env_config('TEST_ENV_VAR', logger=test_logger, default='default_value', required=True, var_type=str, custom_message=None)
def sample_function(env_var_value=None):
    return f"Function executed with env_var_value: {env_var_value}"

def test_valid_types():
    """
    Test case 1: Valid types for arguments and return value
    """
    result = sample_function(1, "test")
    assert result == "1 - test"

def test_invalid_argument_type():
    """
    Test case 2: Invalid type for argument, no logger provided
    """
    @enforce_types()
    def sample_function_invalid_arg(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with pytest.raises(TypeError, match="Argument 'a' must be of type int"):
        sample_function_invalid_arg("invalid", "test")

def test_invalid_return_type():
    """
    Test case 3: Invalid type for return value, no logger provided
    """
    @enforce_types()
    def sample_function_invalid_return(a: int, b: str) -> int:
        return f"{a} - {b}"
    
    with pytest.raises(TypeError, match="Return value must be of type int"):
        sample_function_invalid_return(1, "test")

def test_invalid_argument_type_with_logger(caplog):
    """
    Test case 4: Invalid type for argument, with logger
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
    Test case 5: Invalid type for return value, with logger
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
    Test case 6: Invalid type for argument with kwargs, no logger provided
    """
    @enforce_types()
    def sample_function_invalid_arg_kwargs(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with pytest.raises(TypeError, match="Argument 'a' must be of type int"):
        sample_function_invalid_arg_kwargs(a="invalid", b="test")

def test_invalid_argument_type_with_kwargs_and_logger(caplog):
    """
    Test case 7: Invalid type for argument with kwargs, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_invalid_arg_kwargs_with_logger(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match="Argument 'a' must be of type int"):
            sample_function_invalid_arg_kwargs_with_logger(a="invalid", b="test")
    assert "Argument 'a' must be of type int" in caplog.text

def test_valid_types_with_kwargs():
    """
    Test case 8: Valid types for arguments with kwargs
    """
    @enforce_types()
    def sample_function_valid_kwargs(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    result = sample_function_valid_kwargs(a=1, b="test")
    assert result == "1 - test"

def test_valid_types_with_kwargs_and_logger(caplog):
    """
    Test case 9: Valid types for arguments with kwargs, with logger
    """
    @enforce_types(logger=test_logger)
    def sample_function_valid_kwargs_with_logger(a: int, b: str) -> str:
        return f"{a} - {b}"
    
    with caplog.at_level(logging.INFO):
        result = sample_function_valid_kwargs_with_logger(a=1, b="test")
    assert result == "1 - test"
    assert "Argument 'a' must be of type int" not in caplog.text
    assert "Return value must be of type int" not in caplog.text

def test_missing_type_annotations():
    """
    Test case 10: Function without type annotations
    """
    @enforce_types()
    def sample_function_no_annotations(a, b):
        return f"{a} - {b}"
    
    result = sample_function_no_annotations(1, "test")
    assert result == "1 - test"

def test_mixed_valid_and_invalid_arguments():
    """
    Test case 11: Mixed valid and invalid arguments
    """
    @enforce_types()
    def sample_function_mixed_args(a: int, b: str, c: float) -> str:
        return f"{a} - {b} - {c}"
    
    with pytest.raises(TypeError, match="Argument 'c' must be of type float"):
        sample_function_mixed_args(1, "test", "invalid")

def test_default_argument_values():
    """
    Test case 12: Function with default argument values
    """
    @enforce_types()
    def sample_function_default_args(a: int, b: str = "default") -> str:
        return f"{a} - {b}"
    
    result = sample_function_default_args(1)
    assert result == "1 - default"

def test_variable_length_arguments():
    """
    Test case 13: Function with variable length arguments (*args and **kwargs)
    """
    @enforce_types()
    def sample_function_var_args(a: int, *args: str, **kwargs: float) -> str:
        return f"{a} - {args} - {kwargs}"
    
    result = sample_function_var_args(1, "arg1", "arg2", kwarg1=1.0, kwarg2=2.0)
    assert result == "1 - ('arg1', 'arg2') - {'kwarg1': 1.0, 'kwarg2': 2.0}"

def test_invalid_logger():
    """
    Test case 14: Invalid logger (not an instance of logging.Logger or None)
    """
    # Test case 14: Invalid logger (not an instance of logging.Logger or None)
    with pytest.raises(TypeError, match="logger must be an instance of logging.Logger or None"):
        @env_config('TEST_ENV_VAR', logger="not_a_logger")
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_var_name():
    """
    Test case 15: Invalid var_name (not a non-empty string), no logger provided
    """
    # Test case 15: Invalid var_name (not a non-empty string), no logger provided
    with pytest.raises(TypeError, match="var_name must be a non-empty string"):
        @env_config(123)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_required():
    """
    Test case 16: Invalid required (not a boolean), no logger provided
    """
    # Test case 16: Invalid required (not a boolean), no logger provided
    with pytest.raises(TypeError, match="required must be a boolean"):
        @env_config('TEST_ENV_VAR', required="not_a_boolean")
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_var_type():
    """
    Test case 17: Invalid var_type (not a type), no logger provided
    """
    # Test case 13: Invalid var_type (not a type), no logger provided
    with pytest.raises(TypeError, match="var_type must be a type"):
        @env_config('TEST_ENV_VAR', var_type="not_a_type")
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_custom_message():
    """
    Test case 17: Invalid custom_message (not a string or None), no logger provided
    """
    # Test case 14: Invalid custom_message (not a string or None), no logger provided
    with pytest.raises(TypeError, match="custom_message must be a string or None"):
        @env_config('TEST_ENV_VAR', custom_message=123)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_var_name_with_logger(caplog):
    """
    Test case 18: Invalid var_name (not a non-empty string), logger provided
    """
    # Test case 18: Invalid var_name (not a non-empty string), logger provided
    with caplog.at_level(logging.ERROR):
        @env_config(123, logger=test_logger)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
        with pytest.raises(TypeError):
            sample_function()
    assert "var_name must be a non-empty string" in caplog.text

def test_invalid_required_with_logger(caplog):
    """
    Test case 19: Invalid required (not a boolean), logger provided
    """
    # Test case 19: Invalid required (not a boolean), logger provided
    with caplog.at_level(logging.ERROR):
        @env_config('TEST_ENV_VAR', required="not_a_boolean", logger=test_logger)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
        with pytest.raises(TypeError):
            sample_function()
    assert "required must be a boolean" in caplog.text

def test_invalid_var_type_with_logger(caplog):
    """
    Test case 20: Invalid var_type (not a type), logger provided
    """
    # Test case 20: Invalid var_type (not a type), logger provided
    with caplog.at_level(logging.ERROR):
        @env_config('TEST_ENV_VAR', var_type="not_a_type", logger=test_logger)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
        with pytest.raises(TypeError):
            sample_function()
    assert "var_type must be a type" in caplog.text

def test_invalid_custom_message_with_logger(caplog):
    """
    Test case 21: Invalid custom_message (not a string or None), logger provided
    """
    # Test case 21: Invalid custom_message (not a string or None), logger provided
    with caplog.at_level(logging.ERROR):
        @env_config('TEST_ENV_VAR', custom_message=123, logger=test_logger)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
        with pytest.raises(TypeError):
            sample_function()
    assert "custom_message must be a string or None" in caplog.text
