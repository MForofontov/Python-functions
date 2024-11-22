import zstandard as zstd

def compress_zstd(data: str, level: int = 3, encoding: str = 'utf-8') -> bytes:
    """
    Compress a string using Zstandard (zstd).

    Parameters
    ----------
    data : str
        The string to be compressed.
    level : int, optional
        The compression level (default is 3).
    encoding : str, optional
        The encoding to use for the string (default is 'utf-8').

    Returns
    -------
    bytes
        The compressed data as bytes.

    Raises
    ------
    TypeError
        If data is not a string, level is not an integer, or encoding is not a string.
    ValueError
        If an error occurs during compression.
    """
    if not isinstance(data, str):
        raise TypeError("data must be a string")
    if not isinstance(level, int):
        raise TypeError("level must be an integer")
    if not isinstance(encoding, str):
        raise TypeError("encoding must be a string")

    try:
        compressor = zstd.ZstdCompressor(level=level)
        compressed: bytes = compressor.compress(data.encode(encoding))
        return compressed
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")
