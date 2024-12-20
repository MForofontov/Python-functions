import pytest
import asyncio
import logging
from decorators.async_wrapper import async_wrapper

# Configure test_logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

def sync_function(x: int, y: int) -> int:
    """
    Synchronous function that adds two numbers.
    """
    return x + y

def sync_function_with_error(x: int, y: int) -> None:
    """
    Synchronous function that raises a ValueError.
    """
    raise ValueError("This is an example error")

async def async_function(x: int, y: int) -> int:
    """
    Asynchronous function that adds two numbers.
    """
    return x + y

@async_wrapper
def wrapped_sync_function(x: int, y: int) -> int:
    """
    Wrapped synchronous function that adds two numbers.
    """
    return sync_function(x, y)

@async_wrapper
def wrapped_sync_function_with_error(x: int, y: int) -> None:
    """
    Wrapped synchronous function that raises a ValueError.
    """
    return sync_function_with_error(x, y)

@async_wrapper(test_logger)
def wrapped_sync_function_with_logging(x: int, y: int) -> None:
    """
    Wrapped synchronous function that raises a ValueError with logging enabled.
    """
    return sync_function_with_error(x, y)

@pytest.mark.asyncio
async def test_async_wrapper_success():
    """
    Test the async_wrapper decorator with a synchronous function that succeeds.
    """
    # Test case 1: Synchronous function that succeeds
    result = await wrapped_sync_function(1, 2)
    assert result == 3

@pytest.mark.asyncio
async def test_async_wrapper_with_logging(caplog):
    """
    Test the async_wrapper decorator with logging enabled.
    """
    # Test case 2: Synchronous function that raises an error with logging enabled
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError, match="This is an example error"):
            await wrapped_sync_function_with_logging(1, 2)
        assert "An error occurred in wrapped_sync_function_with_logging: This is an example error" in caplog.text

def test_async_wrapper_invalid_function(caplog):
    """
    Test the async_wrapper decorator with an asynchronous function.
    """
    # Test case 3: Asynchronous function passed to async_wrapper
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match="The function to be wrapped must be synchronous"):
            @async_wrapper(test_logger)
            async def invalid_function(x: int, y: int) -> int:
                return await async_function(x, y)
        assert "An error occurred in invalid_function: The function to be wrapped must be synchronous" in caplog.text

@pytest.mark.asyncio
async def test_async_wrapper_error():
    """
    Test the async_wrapper decorator with a synchronous function that raises an error.
    """
    # Test case 4: Synchronous function that raises an error
    with pytest.raises(ValueError, match="This is an example error"):
        await wrapped_sync_function_with_error(1, 2)
