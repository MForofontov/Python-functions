import zlib
import base64
from typing import Any

def decompress_zlib(compressed_data: str, encoding: str = 'utf-8') -> str:
    """
    Decompress a base64-encoded, zlib-compressed string.

    Parameters
    ----------
    compressed_data : str
        The compressed and base64-encoded string.
    encoding : str, optional
        The encoding to use for the decompressed string (default is 'utf-8').

    Returns
    -------
    str
        The decompressed string.

    Raises
    ------
    TypeError
        If compressed_data is not a string or encoding is not a string.
    ValueError
        If an error occurs during decompression.
    """
    if not isinstance(compressed_data, str):
        raise TypeError("compressed_data must be a string")
    if not isinstance(encoding, str):
        raise TypeError("encoding must be a string")

    try:
        compressed: bytes = base64.b64decode(compressed_data)
        decompressed: str = zlib.decompress(compressed).decode(encoding)
        return decompressed
    except Exception as e:
        raise ValueError(f"An error occurred during decompression: {e}")