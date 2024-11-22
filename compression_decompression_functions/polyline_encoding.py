from typing import List

def polyline_encoding(numbers: List[float], precision: int = 5) -> str:
    """
    Encode a list of floating-point numbers using polyline encoding.

    Parameters
    ----------
    numbers : List[float]
        List of floating-point numbers to be encoded.
    precision : int, optional
        The precision of the encoded numbers (default is 5).

    Returns
    -------
    str
        The encoded polyline string.

    Raises
    ------
    ValueError
        If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty.")

    encoded_text = chr(precision + 63)
    last_number = 0

    for number in numbers:
        scaled_number = int(round(number * (10 ** precision)))
        delta = scaled_number - last_number
        last_number = scaled_number

        # Encode the delta using the polyline encoding scheme
        delta = ~(delta << 1) if delta < 0 else (delta << 1)
        while delta >= 0x20:
            encoded_text += chr((0x20 | (delta & 0x1f)) + 63)
            delta >>= 5
        encoded_text += chr(delta + 63)

    return encoded_text
