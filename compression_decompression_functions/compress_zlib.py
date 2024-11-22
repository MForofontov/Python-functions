import zlib
import base64

def compress_zlib(data: str, encoding: str = 'utf-8') -> str:
    """
    Compress a string using zlib and encode it with base64.

    Parameters
    ----------
    data : str
        The string to be compressed.
    encoding : str, optional
        The encoding to use for the string (default is 'utf-8').

    Returns
    -------
    str
        The compressed and base64-encoded string.

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
        compressed: bytes = zlib.compress(data.encode(encoding))
        encoded: str = base64.b64encode(compressed).decode(encoding)
        return encoded
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")