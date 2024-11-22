import gzip
import io

def compress_gzip(data: bytes) -> bytes:
    """
    Compress data using gzip.

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
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode='wb') as gzip_file:
            gzip_file.write(data)
        return buffer.getvalue()
    except Exception as e:
        raise ValueError(f"An error occurred during compression: {e}")
