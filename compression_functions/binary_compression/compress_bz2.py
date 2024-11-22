import bz2

def compress_bz2(data: bytes) -> bytes:
    """
    Compress data using bz2.

    Parameters
    ----------
    data : bytes
        The data to be compressed.

    Returns
    -------
    bytes
        The compressed data as bytes.

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
        compressed: bytes = bz2.compress(data)
        return compressed
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")
