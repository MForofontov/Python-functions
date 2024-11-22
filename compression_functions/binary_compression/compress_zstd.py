import zstandard as zstd

def compress_zstd(data: bytes, level: int = 3) -> bytes:
    """
    Compress data using Zstandard (zstd).

    Parameters
    ----------
    data : bytes
        The data to be compressed.
    level : int, optional
        The compression level (default is 3).

    Returns
    -------
    bytes
        The compressed data as bytes.

    Raises
    ------
    TypeError
        If data is not bytes or level is not an integer.
    ValueError
        If an error occurs during compression.
    """
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")
    if not isinstance(level, int):
        raise TypeError("level must be an integer")

    try:
        compressor = zstd.ZstdCompressor(level=level)
        compressed: bytes = compressor.compress(data)
        return compressed
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")
