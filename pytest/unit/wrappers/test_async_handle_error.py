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

# Test case 1: Asynchronous function that succeeds
@pytest.mark.asyncio
async def test_async_function_success():
    """
    Test case 1: Asynchronous function that succeeds
    """
    result = await sample_function_success(1, 2)
    assert result == 3

# Test case 2: Asynchronous function that raises an exception
@pytest.mark.asyncio
async def test_async_function_exception(capfd):
    """
    Test case 2: Asynchronous function that raises an exception
    """
    result = await sample_function_exception(1, 2)
    assert result is None
    captured = capfd.readouterr()
    assert "An error occurred: Test exception" in captured.out

# Test case 3: Synchronous function that raises an error
@pytest.mark.asyncio
async def test_non_async_function():
    """
    Test case 3: Synchronous function that raises an error
    """
    with pytest.raises(TypeError, match="The function to be wrapped must be asynchronous"):
        @async_handle_error("An error occurred")
        def sample_function(x: int, y: int) -> int:
            return x + y

# Test case 4: Asynchronous function that raises an exception with logging enabled
@pytest.mark.asyncio
async def test_async_function_with_logger(caplog):
    """
    Test case 4: Asynchronous function that raises an exception with logging enabled
    """
    with caplog.at_level(logging.ERROR):
        result = await sample_function_with_logger(1, 2)
        assert result is None
        assert "An error occurred: Test exception" in caplog.text

# Test case 5: Asynchronous function with positional arguments
@pytest.mark.asyncio
async def test_async_function_with_args():
    """
    Test case 5: Asynchronous function with positional arguments
    """
    result = await sample_function_with_args(1, 2, 3)
    assert result == 6

# Test case 6: Asynchronous function with keyword arguments
@pytest.mark.asyncio
async def test_async_function_with_kwargs():
    """
    Test case 6: Asynchronous function with keyword arguments
    """
    result = await sample_function_with_kwargs(1, 2, z=3)
    assert result == 6

# Test case 7: Asynchronous function with mixed positional and keyword arguments
@pytest.mark.asyncio
async def test_async_function_with_mixed_args_kwargs():
    """
    Test case 7: Asynchronous function with mixed positional and keyword arguments
    """
    result = await sample_function_with_mixed_args_kwargs(1, 2, 3, 4, z=5, a=6, b=7)
    assert result == 28

# Test case 8: Asynchronous function with no arguments
@pytest.mark.asyncio
async def test_async_function_with_no_args():
    """
    Test case 8: Asynchronous function with no arguments
    """
    result = await sample_function_no_args()
    assert result == "success"