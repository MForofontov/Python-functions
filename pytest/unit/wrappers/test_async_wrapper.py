import pytest
import asyncio
import logging
from decorators.async_wrapper import async_wrapper

def sync_function(x, y):
    return x + y

def sync_function_with_error(x, y):
    raise ValueError("This is an example error")

async def async_function(x, y):
    return x + y

@async_wrapper
def wrapped_sync_function(x, y):
    return sync_function(x, y)

@async_wrapper
def wrapped_sync_function_with_error(x, y):
    return sync_function_with_error(x, y)

@async_wrapper(log_errors=True)
def wrapped_sync_function_with_logging(x, y):
    return sync_function_with_error(x, y)

@pytest.mark.asyncio
async def test_async_wrapper_success():
    """
    Test the async_wrapper decorator with a synchronous function that succeeds.
    """
    result = await wrapped_sync_function(1, 2)
    assert result == 3

@pytest.mark.asyncio
async def test_async_wrapper_with_logging(caplog):
    """
    Test the async_wrapper decorator with logging enabled.
    """
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError, match="This is an example error"):
            await wrapped_sync_function_with_logging(1, 2)
        assert "An error occurred in wrapped_sync_function_with_logging: This is an example error" in caplog.text

def test_async_wrapper_invalid_function(caplog):
    """
    Test the async_wrapper decorator with an asynchronous function.
    """
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match="The function to be wrapped must be synchronous"):
            @async_wrapper(log_errors=True)
            async def invalid_function(x, y):
                return await async_function(x, y)
        assert "An error occurred in invalid_function: The function to be wrapped must be synchronous" in caplog.text

@pytest.mark.asyncio
async def test_async_wrapper_error():
    """
    Test the async_wrapper decorator with a synchronous function that raises an error.
    """
    with pytest.raises(ValueError, match="This is an example error"):
        await wrapped_sync_function_with_error(1, 2)
