import os
import pytest
import logging
from decorators.env_config import env_config

# Configure test_logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

# Sample function to be decorated
@env_config('TEST_ENV_VAR', logger=test_logger, default='default_value', required=False, var_type=str, custom_message="Custom log message")
def sample_function(env_var_value=None):
    return f"Function executed with env_var_value: {env_var_value}"

def test_env_var_set(monkeypatch, caplog):
    """
    Test case 1: Environment variable is set
    """
    # Test case 1: Environment variable is set
    monkeypatch.setenv('TEST_ENV_VAR', 'test_value')
    with caplog.at_level(logging.INFO):
        result = sample_function()
    assert result == "Function executed with env_var_value: test_value"
    assert "Custom log message" in caplog.text

def test_env_var_not_set(monkeypatch, caplog):
    """
    Test case 2: Environment variable is not set
    """
    # Test case 2: Environment variable is not set
    monkeypatch.delenv('TEST_ENV_VAR', raising=False)
    with caplog.at_level(logging.INFO):
        result = sample_function()
    assert result == "Function executed with env_var_value: default_value"
    assert "Custom log message" in caplog.text

def test_env_var_required(monkeypatch, caplog):
    """
    Test case 3: Required environment variable is not set
    """
    # Test case 3: Required environment variable is not set
    monkeypatch.delenv('TEST_ENV_VAR', raising=False)
    with caplog.at_level(logging.ERROR):
        @env_config('TEST_ENV_VAR', logger=test_logger, required=True)
        def sample_function_required(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
        result = sample_function_required()
    assert result is None
    assert "Required environment variable TEST_ENV_VAR is not set" in caplog.text

def test_env_var_type_conversion(monkeypatch, caplog):
    """
    Test case 4: Environment variable type conversion
    """
    # Test case 4: Environment variable type conversion
    monkeypatch.setenv('TEST_ENV_VAR', '123')
    @env_config('TEST_ENV_VAR', logger=test_logger, var_type=int)
    def sample_function_type(env_var_value=None):
        return f"Function executed with env_var_value: {env_var_value}"
    with caplog.at_level(logging.INFO):
        result = sample_function_type()
    assert result == "Function executed with env_var_value: 123"
    assert "Using environment variable TEST_ENV_VAR with value: 123" in caplog.text

def test_env_var_invalid_type_conversion(monkeypatch, caplog):
    """
    Test case 5: Invalid environment variable type conversion
    """
    # Test case 5: Invalid environment variable type conversion
    monkeypatch.setenv('TEST_ENV_VAR', 'invalid_int')
    with caplog.at_level(logging.ERROR):
        @env_config('TEST_ENV_VAR', logger=test_logger, var_type=int)
        def sample_function_invalid_type(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
        result = sample_function_invalid_type()
    assert result is None
    assert "Environment variable TEST_ENV_VAR cannot be converted to int" in caplog.text

def test_env_var_no_logger(monkeypatch, capsys):
    """
    Test case 6: Environment variable is set, no logger provided
    """
    # Test case 6: Environment variable is set, no logger provided
    monkeypatch.setenv('TEST_ENV_VAR', 'test_value')
    @env_config('TEST_ENV_VAR', default='default_value', required=False, var_type=str, custom_message="Custom log message")
    def sample_function_no_logger(env_var_value=None):
        return f"Function executed with env_var_value: {env_var_value}"
    result = sample_function_no_logger()
    captured = capsys.readouterr()
    assert result == "Function executed with env_var_value: test_value"
    assert "Custom log message" in captured.out

def test_env_var_not_set_no_logger(monkeypatch, capsys):
    """
    Test case 7: Environment variable is not set, no logger provided
    """
    # Test case 7: Environment variable is not set, no logger provided
    monkeypatch.delenv('TEST_ENV_VAR', raising=False)
    @env_config('TEST_ENV_VAR', default='default_value', required=False, var_type=str, custom_message="Custom log message")
    def sample_function_no_logger(env_var_value=None):
        return f"Function executed with env_var_value: {env_var_value}"
    result = sample_function_no_logger()
    captured = capsys.readouterr()
    assert result == "Function executed with env_var_value: default_value"
    assert "Custom log message" in captured.out

def test_env_var_required_no_logger(monkeypatch, capsys):
    """
    Test case 8: Required environment variable is not set, no logger provided
    """
    # Test case 8: Required environment variable is not set, no logger provided
    monkeypatch.delenv('TEST_ENV_VAR', raising=False)
    @env_config('TEST_ENV_VAR', required=True)
    def sample_function_required_no_logger(env_var_value=None):
        return f"Function executed with env_var_value: {env_var_value}"
    with pytest.raises(ValueError):
        sample_function_required_no_logger()

def test_env_var_invalid_type_conversion_no_logger(monkeypatch, capsys):
    """
    Test case 9: Invalid environment variable type conversion, no logger provided
    """
    # Test case 9: Invalid environment variable type conversion, no logger provided
    monkeypatch.setenv('TEST_ENV_VAR', 'invalid_int')
    @env_config('TEST_ENV_VAR', var_type=int)
    def sample_function_invalid_type_no_logger(env_var_value=None):
        return f"Function executed with env_var_value: {env_var_value}"
    with pytest.raises(ValueError):
        sample_function_invalid_type_no_logger()

def test_invalid_var_name():
    """
    Test case 10: Invalid var_name (not a non-empty string)
    """
    with pytest.raises(TypeError, match="var_name must be a non-empty string"):
        @env_config(123)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_logger():
    """
    Test case 11: Invalid logger (not an instance of logging.Logger or None)
    """
    with pytest.raises(TypeError, match="logger must be an instance of logging.Logger or None"):
        @env_config('TEST_ENV_VAR', logger="not_a_logger")
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_required():
    """
    Test case 12: Invalid required (not a boolean)
    """
    with pytest.raises(TypeError, match="required must be a boolean"):
        @env_config('TEST_ENV_VAR', required="not_a_boolean")
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_var_type():
    """
    Test case 12: Invalid var_type (not a type)
    """
    with pytest.raises(TypeError, match="var_type must be a type"):
        @env_config('TEST_ENV_VAR', var_type="not_a_type")
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"

def test_invalid_custom_message():
    """
    Test case 13: Invalid custom_message (not a string or None)
    """
    with pytest.raises(TypeError, match="custom_message must be a string or None"):
        @env_config('TEST_ENV_VAR', custom_message=123)
        def sample_function(env_var_value=None):
            return f"Function executed with env_var_value: {env_var_value}"
