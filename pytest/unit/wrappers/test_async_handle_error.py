import pytest
import asyncio
import os
from decorators.async_handle_error import async_handle_error

@async_handle_error("An error occurred in example_coroutine")
async def example_coroutine():
    await asyncio.sleep(1)
    raise ValueError("This is an example error")

@async_handle_error("An error occurred in example_coroutine_no_error")
async def example_coroutine_no_error():
    await asyncio.sleep(1)
    return "Success"

@async_handle_error("An error occurred in example_coroutine_with_logging", log_file="error.log")
async def example_coroutine_with_logging():
    await asyncio.sleep(1)
    raise ValueError("This is an example error with logging")

@pytest.mark.asyncio
async def test_async_handle_error_with_error(capfd):
    """
    Test the async_handle_error decorator with a function that raises an error.
    """
    result = await example_coroutine()
    assert result is None

    # Capture the printed output
    captured = capfd.readouterr()
    assert "An error occurred in example_coroutine: This is an example error" in captured.out

@pytest.mark.asyncio
async def test_async_handle_error_no_error():
    """
    Test the async_handle_error decorator with a function that does not raise an error.
    """
    result = await example_coroutine_no_error()
    assert result == "Success"

@pytest.mark.asyncio
async def test_async_handle_error_with_logging(capfd):
    """
    Test the async_handle_error decorator with logging enabled.
    """
    result = await example_coroutine_with_logging()
    assert result is None

    # Capture the printed output
    captured = capfd.readouterr()
    assert "An error occurred in example_coroutine_with_logging: This is an example error with logging" in captured.out

    # Check if the log file contains the error message
    with open("error.log", "r") as log_file:
        log_content = log_file.read()
        assert "An error occurred in example_coroutine_with_logging" in log_content
        assert "This is an example error with logging" in log_content

    # Clean up: delete the log file
    os.remove("error.log")

def test_async_handle_error_invalid_function():
    """
    Test the async_handle_error decorator with a non-async function.
    """
    with pytest.raises(TypeError):
        @async_handle_error("An error occurred in invalid_function")
        def invalid_function():
            pass
