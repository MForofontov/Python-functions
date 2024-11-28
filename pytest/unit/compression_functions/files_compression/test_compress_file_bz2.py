import pytest
import bz2
import os
from compression_functions.files_compression.compress_file_bz2 import compress_file_bz2

def test_compress_file_bz2_basic(tmp_path) -> None:
    """
    Test the compress_file_bz2 function with basic input.
    """
    # Test case 1: Basic compression
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.bz2"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    compress_file_bz2(str(input_file), str(output_file))
    
    with bz2.open(output_file, 'rb') as f:
        compressed_data = f.read()
    
    assert compressed_data == data, "Decompressed data should match the original data"

def test_compress_file_bz2_empty(tmp_path) -> None:
    """
    Test the compress_file_bz2 function with an empty file.
    """
    # Test case 2: Empty file
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.bz2"
    
    with open(input_file, 'wb') as f:
        pass
    
    compress_file_bz2(str(input_file), str(output_file))
    
    with bz2.open(output_file, 'rb') as f:
        compressed_data = f.read()
    
    assert compressed_data == b"", "Decompressed data should match the original data"

def test_compress_file_bz2_large_file(tmp_path) -> None:
    """
    Test the compress_file_bz2 function with a large file.
    """
    # Test case 3: Large file compression
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.bz2"
    data = b"a" * 1000000  # 1 MB of data
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    compress_file_bz2(str(input_file), str(output_file))
    
    with bz2.open(output_file, 'rb') as f:
        compressed_data = f.read()
    
    assert compressed_data == data, "Decompressed data should match the original data"

def test_compress_file_bz2_invalid_input_type(tmp_path) -> None:
    """
    Test the compress_file_bz2 function with invalid input file type.
    """
    # Test case 4: Invalid input file type
    output_file = tmp_path / "output.bz2"
    
    with pytest.raises(TypeError):
        compress_file_bz2(123, str(output_file))  # type: ignore

def test_compress_file_bz2_invalid_output_type(tmp_path) -> None:
    """
    Test the compress_file_bz2 function with invalid output file type.
    """
    # Test case 5: Invalid output file type
    input_file = tmp_path / "input.txt"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with pytest.raises(TypeError):
        compress_file_bz2(str(input_file), 123)  # type: ignore

def test_compress_file_bz2_file_not_found(tmp_path) -> None:
    """
    Test the compress_file_bz2 function with a non-existent input file.
    """
    # Test case 6: Non-existent input file
    input_file = tmp_path / "non_existent.txt"
    output_file = tmp_path / "output.bz2"
    
    with pytest.raises(FileNotFoundError):
        compress_file_bz2(str(input_file), str(output_file))

def test_compress_file_bz2_io_error(tmp_path) -> None:
    """
    Test the compress_file_bz2 function handling of I/O errors.
    """
    # Test case 7: Handling of I/O errors
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.bz2"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    # Simulate an I/O error by making the output directory read-only
    os.chmod(tmp_path, 0o400)
    
    try:
        with pytest.raises(IOError):
            compress_file_bz2(str(input_file), str(output_file))
    finally:
        # Restore permissions to delete the temporary directory
        os.chmod(tmp_path, 0o700)
