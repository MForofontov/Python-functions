import zlib
import base64

def compress_zlib(data: bytes) -> bytes:
    """
    Compress data using zlib and encode it with base64.

    Parameters
    ----------
    data : bytes
        The data to be compressed.

    Returns
    -------
    bytes
        The compressed and base64-encoded data as bytes.

    Raises
    ------
    TypeError
        If data is not bytes.
    ValueError
        If an error occurs during compression.
    """
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")

    try:
        compressed: bytes = zlib.compress(data)
        encoded: bytes = base64.b64encode(compressed)
        return encoded
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")
