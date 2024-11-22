import bz2

def compress_bz2(data: str, encoding: str = 'utf-8') -> bytes:
    """
    Compress a string using bz2.

    Parameters
    ----------
    data : str
        The string to be compressed.
    encoding : str, optional
        The encoding to use for the string (default is 'utf-8').

    Returns
    -------
    bytes
        The compressed data as bytes.

    Raises
    ------
    TypeError
        If data is not a string or encoding is not a string.
    ValueError
        If an error occurs during compression.
    """
    if not isinstance(data, str):
        raise TypeError("data must be a string")
    if not isinstance(encoding, str):
        raise TypeError("encoding must be a string")

    try:
        compressed: bytes = bz2.compress(data.encode(encoding))
        return compressed
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")