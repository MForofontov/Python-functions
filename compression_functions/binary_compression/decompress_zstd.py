import zstandard as zstd
def decompress_zstd(compressed_data: bytes) -> bytes:
    """
    Decompress Zstandard (zstd)-compressed data.

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
        decompressor = zstd.ZstdDecompressor()
        decompressed: bytes = decompressor.decompress(compressed_data)
        return decompressed
    except Exception as e:
        raise ValueError(f"An error occurred during decompression: {e}")
