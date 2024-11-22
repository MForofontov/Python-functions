import gzip
import io

def compress_gzip(data: str, encoding: str = 'utf-8') -> bytes:
    """
    Compress a string using gzip.

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
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode='wb') as gzip_file:
            gzip_file.write(data.encode(encoding))
        return buffer.getvalue()
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")