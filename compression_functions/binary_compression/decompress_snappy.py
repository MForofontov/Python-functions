import snappy

def decompress_snappy(compressed_data: bytes) -> bytes:
    """
    Decompress Snappy-compressed data.

    Parameters
    ----------
    compressed_data : bytes
        The compressed data as bytes.

    Returns
    -------
    bytes
        The decompressed data as bytes.

    Raises
    ------
    TypeError
        If compressed_data is not bytes.
    ValueError
        If an error occurs during decompression.
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("compressed_data must be bytes")

    try:
        decompressed: bytes = snappy.decompress(compressed_data)
        return decompressed
    except Exception as e:
        raise ValueError(f"An error occurred during decompression: {e}")