import pytest
import warnings
import logging
from decorators.deprecated import deprecated

# Configure a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
test_logger.addHandler(handler)

@deprecated(logger=test_logger)
def old_function(x: int, y: int) -> int:
    """
    Example deprecated function that adds two integers.

    Parameters
    ----------
    x : int
        First integer.
    y : int
        Second integer.

    Returns
    -------
    int
        The sum of x and y.
    """
    return x + y

@deprecated()
def another_old_function(text: str) -> str:
    """
    Example deprecated function that returns a greeting message.

    Parameters
    ----------
    text : str
        The input text.

    Returns
    -------
    str
        A greeting message.
    """
    return f"Hello, {text}!"

def test_old_function(capsys, caplog):
    """
    Test the deprecated decorator with the old_function.
    """
    # Test case 1: Verify the old_function is deprecated
    with caplog.at_level(logging.WARNING):
        result = old_function(1, 2)
        assert result == 3
        assert "Call to deprecated function old_function." in caplog.text

def test_another_old_function(capsys):
    """
    Test the deprecated decorator with the another_old_function.
    """
    # Test case 2: Verify the another_old_function is deprecated
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = another_old_function("world")
        assert result == "Hello, world!"
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert "another_old_function is deprecated." in str(w[-1].message)
