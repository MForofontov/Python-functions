import pytest
import asyncio
import logging
from decorators.async_handle_error import async_handle_error

# Configure test_logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

# Define sample functions for use in tests
@async_handle_error("An error occurred")
async def sample_function_success(x: int, y: int) -> int:
    return x + y

@async_handle_error("An error occurred")
async def sample_function_exception(x: int, y: int) -> int:
    raise ValueError("Test exception")

@async_handle_error("An error occurred", logger=test_logger)
async def sample_function_with_logger(x: int, y: int) -> int:
    raise ValueError("Test exception")

@async_handle_error("An error occurred")
async def sample_function_with_args(x: int, y: int, z: int) -> int:
    return x + y + z

@async_handle_error("An error occurred")
async def sample_function_with_kwargs(x: int, y: int, z: int = 0) -> int:
    return x + y + z

@async_handle_error("An error occurred")
async def sample_function_with_mixed_args_kwargs(x: int, y: int, *args: int, z: int = 0, **kwargs: int) -> int:
    return x + y + z + sum(args) + sum(kwargs.values())

@async_handle_error("An error occurred")
async def sample_function_no_args() -> str:
    return "success"

@pytest.mark.asyncio
async def test_sync_function_success():
    """
    Test case 1: Synchronous function that succeeds
    """
    # Test case 1: Synchronous function that succeeds
    result = await sample_function_success(1, 2)
    assert result == 3

@pytest.mark.asyncio
async def test_sync_function_with_args():
    """
    Test case 2: Synchronous function with positional arguments
    """
    # Test case 2: Synchronous function with positional arguments
    result = await sample_function_with_args(1, 2, 3)
    assert result == 6

@pytest.mark.asyncio
async def test_sync_function_with_kwargs():
    """
    Test case 3: Synchronous function with keyword arguments
    """
    # Test case 3: Synchronous function with keyword arguments
    result = await sample_function_with_kwargs(1, 2, z=3)
    assert result == 6

@pytest.mark.asyncio
async def test_sync_function_with_mixed_args_kwargs():
    """
    Test case 4: Synchronous function with mixed positional and keyword arguments
    """
    # Test case 4: Synchronous function with mixed positional and keyword arguments
    result = await sample_function_with_mixed_args_kwargs(1, 2, 3, 4, z=5, a=6, b=7)
    assert result == 28

@pytest.mark.asyncio
async def test_sync_function_with_no_args():
    """
    Test case 5: Synchronous function with no arguments
    """
    # Test case 5: Synchronous function with no arguments
    result = await sample_function_no_args()
    assert result == "success"


def test_non_async_function():
    """
    Test case 6: Synchronous function that raises an error
    """
    # Test case 6: Synchronous function that raises an TypeError
    with pytest.raises(TypeError, match="The function to be wrapped must be asynchronous"):
        @async_handle_error("An error occurred")
        def sample_function(x: int, y: int) -> int:
            return x + y

@pytest.mark.asyncio
async def test_async_function_exception():
    """
    Test case 7: Asynchronous function that raises an exception
    """
    # Test case 7: Asynchronous function that raises an ValueError
    with pytest.raises(ValueError, match="Test exception"):
        result = await sample_function_exception(1, 2)
    assert result is None


def test_non_async_function_with_logger(caplog):
    """
    Test case 8: Synchronous function that raises an error with logging enabled
    """
    # Test case 8: Synchronous function that raises an error with logging enabled
    with caplog.at_level(logging.ERROR):
        @async_handle_error("An error occurred", logger=test_logger)
        def sample_function(x: int, y: int) -> int:
            return x + y
        assert "An error occurred in sample_function: The function to be wrapped must be asynchronous" in caplog.text

@pytest.mark.asyncio
async def test_async_function_with_logger(caplog):
    """
    Test case 9: Asynchronous function that raises an exception with logging enabled
    """
    # Test case 9: Asynchronous function that raises an exception with logging enabled
    with caplog.at_level(logging.ERROR):
        result = await sample_function_with_logger(1, 2)
        assert result is None
        assert "An error occurred in sample_function_with_logger: Test exception" in caplog.text
