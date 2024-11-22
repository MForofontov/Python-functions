import gzip
import io

def decompress_gzip(compressed_data: bytes) -> str:
    buf = io.BytesIO(compressed_data)
    with gzip.GzipFile(fileobj=buf, mode='rb') as f:
        return f.read().decode('utf-8')