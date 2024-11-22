import zlib
import base64

def decompress_zlib(compressed_data: bytes) -> bytes:
    """
    Decompress a base64-encoded, zlib-compressed string.

    Parameters
    ----------
    compressed_data : bytes
        The compressed and base64-encoded data as bytes.

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
        compressed: bytes = base64.b64decode(compressed_data)
        decompressed: bytes = zlib.decompress(compressed)
        return decompressed
    except Exception as e:
        raise ValueError(f"An error occurred during decompression: {e}")
