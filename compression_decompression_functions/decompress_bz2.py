import bz2

def decompress_bz2(compressed_data: bytes, encoding: str = 'utf-8') -> str:
    """
    Decompress bz2-compressed data.

    Parameters
    ----------
    compressed_data : bytes
        The compressed data as bytes.
    encoding : str, optional
        The encoding to use for the decompressed string (default is 'utf-8').

    Returns
    -------
    str
        The decompressed string.

    Raises
    ------
    TypeError
        If compressed_data is not bytes or encoding is not a string.
    ValueError
        If an error occurs during decompression.
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("compressed_data must be bytes")
    if not isinstance(encoding, str):
        raise TypeError("encoding must be a string")

    try:
        decompressed: bytes = bz2.decompress(compressed_data)
        return decompressed.decode(encoding)
    except Exception as e:
        raise ValueError(f"An error occurred during decompression: {e}")
