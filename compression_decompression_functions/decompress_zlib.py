import zlib
import base64

def decompress_zlib(compressed_data: str) -> str:
    compressed = base64.b64decode(compressed_data)
    return zlib.decompress(compressed).decode('utf-8')