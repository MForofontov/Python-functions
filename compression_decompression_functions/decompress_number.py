from typing import Tuple

def decompress_number(text: str, index: int) -> Tuple[int, int]:
    """
    Decode a single number from a string created with polyline encoding.

    Parameters
    ----------
    text : str
        String representing a compressed list of numbers.
    index : int
        Index of the first character to start decoding a number.

    Returns
    -------
    tuple
        Index to start decoding the next number and the number decoded
        in the current function call.

    Raises
    ------
    TypeError
        If text is not a string or index is not an integer.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(index, int):
        raise TypeError("index must be an integer")

    number = 0
    bitwise_shift = 0

    while True:
        n = (ord(text[index]) - 63)
        index += 1
        if n >= 0x20:
            n -= 0x20
            number = number | (n << bitwise_shift)
            bitwise_shift += 5
        else:
            break

    number = number | (n << bitwise_shift)
    return index, (~number >> 1) if (number & 1) != 0 else (number >> 1)