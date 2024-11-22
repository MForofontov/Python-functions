import lzma

def compress_lzma(data: bytes) -> bytes:
    """
    Compress data using lzma.

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
        compressed: bytes = lzma.compress(data)
        return compressed
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")
