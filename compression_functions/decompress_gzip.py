import gzip
import io

def decompress_gzip(compressed_data: bytes) -> bytes:
    """
    Decompress gzip-compressed data.

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
        buf = io.BytesIO(compressed_data)
        with gzip.GzipFile(fileobj=buf, mode='rb') as f:
            return f.read()
    except Exception as e:
        raise ValueError(f"An error occurred during decompression: {e}")
