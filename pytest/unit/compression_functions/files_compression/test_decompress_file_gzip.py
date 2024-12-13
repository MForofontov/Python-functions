import pytest
import gzip
import os
from compression_functions.files_compression.decompress_file_gzip import decompress_file_gzip

def test_decompress_file_gzip_basic(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with basic input.
    """
    # Test case 1: Basic decompression
    compressed_file = tmp_path / "input.txt.gz"
    output_file = tmp_path / "output.txt"
    data = b"hello world"
    
    # Create a compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        f.write(data)
    
    decompress_file_gzip(str(compressed_file), str(output_file))
    
    # Check if the output file exists
    assert output_file.exists(), "Output file should exist"
    
    # Read the decompressed data to verify
    with open(output_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == data, "Decompressed data should match the original data"

def test_decompress_file_gzip_empty_file(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with an empty file.
    """
    # Test case 2: Empty file
    compressed_file = tmp_path / "input.txt.gz"
    output_file = tmp_path / "output.txt"
    
    # Create an empty compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        pass
    
    decompress_file_gzip(str(compressed_file), str(output_file))
    
    # Check if the output file exists
    assert output_file.exists(), "Output file should exist"
    
    # Read the decompressed data to verify
    with open(output_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == b"", "Decompressed data should be empty"

def test_decompress_file_gzip_large_file(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with a large file.
    """
    # Test case 3: Large file decompression
    compressed_file = tmp_path / "input.txt.gz"
    output_file = tmp_path / "output.txt"
    data = b"a" * 1000000  # 1 MB of data
    
    # Create a compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        f.write(data)
    
    decompress_file_gzip(str(compressed_file), str(output_file))
    
    # Check if the output file exists
    assert output_file.exists(), "Output file should exist"
    
    # Read the decompressed data to verify
    with open(output_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == data, "Decompressed data should match the original data"

def test_decompress_file_gzip_invalid_input_type(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with invalid input file type.
    """
    # Test case 4: Invalid input file type
    output_file = tmp_path / "output.txt"
    
    with pytest.raises(TypeError):
        decompress_file_gzip(123, str(output_file))  # type: ignore

def test_decompress_file_gzip_invalid_output_type(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with invalid output file type.
    """
    # Test case 5: Invalid output file type
    compressed_file = tmp_path / "input.txt.gz"
    data = b"hello world"
    
    # Create a compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        f.write(data)
    
    with pytest.raises(TypeError):
        decompress_file_gzip(str(compressed_file), 123)  # type: ignore

def test_decompress_file_gzip_non_existent_input_file(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with a non-existent input file.
    """
    # Test case 6: Non-existent input file
    compressed_file = tmp_path / "non_existent.txt.gz"
    output_file = tmp_path / "output.txt"
    
    with pytest.raises(FileNotFoundError):
        decompress_file_gzip(str(compressed_file), str(output_file))

def test_decompress_file_gzip_io_error_on_output_file(tmp_path) -> None:
    """
    Test the decompress_file_gzip function handling of I/O errors on output file.
    """
    # Test case 7: Handling of I/O errors on output file
    compressed_file = tmp_path / "input.txt.gz"
    output_file = tmp_path / "output.txt"
    data = b"hello world"
    
    # Create a compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        f.write(data)
    
    # Simulate an I/O error by making the output directory read-only
    os.chmod(tmp_path, 0o400)
    
    try:
        with pytest.raises(IOError):
            decompress_file_gzip(str(compressed_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary directory
        os.chmod(tmp_path, 0o700)

def test_decompress_file_gzip_no_permission_on_input_file(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with no permission on input file.
    """
    # Test case 8: No permission on input file
    compressed_file = tmp_path / "input.txt.gz"
    output_file = tmp_path / "output.txt"
    data = b"hello world"
    
    # Create a compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        f.write(data)
    
    # Remove all permissions from the input file
    os.chmod(compressed_file, 0o000)
    
    try:
        with pytest.raises(PermissionError):
            decompress_file_gzip(str(compressed_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(compressed_file, 0o600)

def test_decompress_file_gzip_io_error_on_read_only_output_file(tmp_path) -> None:
    """
    Test the decompress_file_gzip function with read-only output file.
    """
    # Test case 9: Read-only output file
    compressed_file = tmp_path / "input.txt.gz"
    output_file = tmp_path / "output.txt"
    data = b"hello world"
    
    # Create a compressed gzip file
    with gzip.open(compressed_file, 'wb') as f:
        f.write(data)
    
    with open(output_file, 'wb') as f:
        pass
    
    # Simulate a read-only output file
    os.chmod(output_file, 0o400)
    
    try:
        with pytest.raises(IOError):
            decompress_file_gzip(str(compressed_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(output_file, 0o600)