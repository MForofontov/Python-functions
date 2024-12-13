import pytest
import gzip
import os
from compression_functions.files_compression.compress_file_gzip import compress_file_gzip

def test_compress_file_gzip_basic_compression(tmp_path) -> None:
    """
    Test the compress_file_gzip function with basic input.
    """
    # Test case 1: Basic compression
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    compress_file_gzip(str(input_file), str(output_file))
    
    # Check if the output file exists
    assert output_file.exists(), "Output file should exist"
    
    # Decompress the data to verify
    with gzip.open(output_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == data, "Decompressed data should match the original data"

def test_compress_file_gzip_empty_file_compression_and_verification(tmp_path) -> None:
    """
    Test the compress_file_gzip function with an empty file.
    """
    # Test case 2: Empty file
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.gz"
    
    with open(input_file, 'wb') as f:
        pass
    
    compress_file_gzip(str(input_file), str(output_file))
    
    # Check if the output file exists
    assert output_file.exists(), "Output file should exist"
    
    # Decompress the data to verify
    with gzip.open(output_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == b"", "Decompressed data should match the original data"

def test_compress_file_gzip_large_file_compression_and_verification(tmp_path) -> None:
    """
    Test the compress_file_gzip function with a large file.
    """
    # Test case 3: Large file compression
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.gz"
    data = b"a" * 1000000  # 1 MB of data
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    compress_file_gzip(str(input_file), str(output_file))
    
    # Check if the output file exists
    assert output_file.exists(), "Output file should exist"
    
    # Check if the compressed file is smaller than the original file
    assert output_file.stat().st_size < input_file.stat().st_size, "Compressed file should be smaller than the original file"
    
    # Decompress the data to verify
    with gzip.open(output_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == data, "Decompressed data should match the original data"

def test_compress_file_gzip_invalid_input_file_type(tmp_path) -> None:
    """
    Test the compress_file_gzip function with invalid input file type.
    """
    # Test case 4: Invalid input file type
    output_file = tmp_path / "output.gz"
    
    with pytest.raises(TypeError):
        compress_file_gzip(123, str(output_file))  # type: ignore

def test_compress_file_gzip_invalid_output_file_type(tmp_path) -> None:
    """
    Test the compress_file_gzip function with invalid output file type.
    """
    # Test case 5: Invalid output file type
    input_file = tmp_path / "input.txt"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with pytest.raises(TypeError):
        compress_file_gzip(str(input_file), 123)  # type: ignore

def test_compress_file_gzip_non_existent_input_file(tmp_path) -> None:
    """
    Test the compress_file_gzip function with a non-existent input file.
    """
    # Test case 6: Non-existent input file
    input_file = tmp_path / "non_existent.txt"
    output_file = tmp_path / "output.gz"
    
    with pytest.raises(FileNotFoundError):
        compress_file_gzip(str(input_file), str(output_file))

def test_compress_file_gzip_io_error_on_output_file(tmp_path) -> None:
    """
    Test the compress_file_gzip function handling of I/O errors on output file.
    """
    # Test case 7: Handling of I/O errors on output file
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    # Simulate an I/O error by making the output directory read-only
    os.chmod(tmp_path, 0o400)
    
    try:
        with pytest.raises(IOError):
            compress_file_gzip(str(input_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary directory
        os.chmod(tmp_path, 0o700)

def test_compress_file_gzip_no_permission_on_input_file(tmp_path) -> None:
    """
    Test the compress_file_gzip function with no permission on input file.
    """
    # Test case 8: No permission on input file
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    # Remove all permissions from the input file
    os.chmod(input_file, 0o000)
    
    try:
        with pytest.raises(PermissionError):
            compress_file_gzip(str(input_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(input_file, 0o600)

def test_compress_file_gzip_io_error_on_read_only_output_file(tmp_path) -> None:
    """
    Test the compress_file_gzip function with read-only output file.
    """
    # Test case 9: Read-only output file
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with open(output_file, 'wb') as f:
        pass
    
    # Simulate a read-only output file
    os.chmod(output_file, 0o400)
    
    try:
        with pytest.raises(IOError):
            compress_file_gzip(str(input_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(output_file, 0o600)
