import pytest
from decorators.event_trigger import EventManager, event_trigger

# Initialize the EventManager
event_manager = EventManager()

# Example callback functions
def callback_one(*args, **kwargs):
    callback_one.called = True
    callback_one.args = args
    callback_one.kwargs = kwargs

def callback_two(*args, **kwargs):
    callback_two.called = True
    callback_two.args = args
    callback_two.kwargs = kwargs

# Reset callback state
def reset_callbacks():
    callback_one.called = False
    callback_one.args = None
    callback_one.kwargs = None
    callback_two.called = False
    callback_two.args = None
    callback_two.kwargs = None

# Subscribe callbacks to events
event_manager.subscribe("event_one", callback_one)
event_manager.subscribe("event_two", callback_two)

@event_trigger("event_one")
def example_function_one(a, b):
    return f"Result: {a + b}"

@event_trigger("event_two")
def example_function_two(a, b):
    return f"Result: {a * b}"

def test_event_trigger_single_callback():
    """
    Test case 1: Single callback triggered
    """
    reset_callbacks()
    result = example_function_one(1, 2)
    assert result == "Result: 3"
    assert callback_one.called
    assert callback_one.args == (1, 2)
    assert callback_one.kwargs == {}

def test_event_trigger_multiple_callbacks():
    """
    Test case 2: Multiple callbacks triggered
    """
    reset_callbacks()
    result = example_function_two(2, 3)
    assert result == "Result: 6"
    assert callback_two.called
    assert callback_two.args == (2, 3)
    assert callback_two.kwargs == {}

def test_event_trigger_no_callbacks():
    """
    Test case 3: No callbacks triggered
    """
    reset_callbacks()
    event_manager.trigger("event_three")
    assert not callback_one.called
    assert not callback_two.called

def test_event_trigger_with_args_and_kwargs():
    """
    Test case 4: Callbacks with arguments and keyword arguments
    """
    reset_callbacks()
    event_manager.trigger("event_one", 1, 2, key="value")
    assert callback_one.called
    assert callback_one.args == (1, 2)
    assert callback_one.kwargs == {"key": "value"}

def test_event_trigger_invalid_event():
    """
    Test case 5: Triggering an invalid event
    """
    reset_callbacks()
    event_manager.trigger("invalid_event")
    assert not callback_one.called
    assert not callback_two.called

def test_event_trigger_decorator():
    """
    Test case 6: Using the event_trigger decorator
    """
    reset_callbacks()
    result = example_function_one(3, 4)
    assert result == "Result: 7"
    assert callback_one.called
    assert callback_one.args == (3, 4)
    assert callback_one.kwargs == {}
