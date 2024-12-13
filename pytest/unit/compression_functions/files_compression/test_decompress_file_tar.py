import pytest
import tarfile
import os
from compression_functions.files_compression.decompress_file_tar import decompress_file_tar

def test_decompress_file_tar_basic(tmp_path) -> None:
    """
    Test the decompress_file_tar function with basic input.
    """
    # Test case 1: Basic decompression
    compressed_file = tmp_path / "input.tar.gz"
    output_dir = tmp_path / "output"
    data = b"hello world"
    
    # Create a tar-compressed file
    os.makedirs(output_dir)
    input_file = tmp_path / "input.txt"
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with tarfile.open(compressed_file, 'w:gz') as tar:
        tar.add(input_file, arcname="input.txt")
    
    decompress_file_tar(str(compressed_file), str(output_dir))
    
    # Check if the output file exists
    extracted_file = output_dir / "input.txt"
    assert extracted_file.exists(), "Extracted file should exist"
    
    # Read the decompressed data to verify
    with open(extracted_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == data, "Decompressed data should match the original data"

def test_decompress_file_tar_empty_file(tmp_path) -> None:
    """
    Test the decompress_file_tar function with an empty file.
    """
    # Test case 2: Empty file
    compressed_file = tmp_path / "input.tar.gz"
    output_dir = tmp_path / "output"
    
    # Create an empty tar-compressed file
    with tarfile.open(compressed_file, 'w:gz') as tar:
        pass
    
    decompress_file_tar(str(compressed_file), str(output_dir))
    
    # Check if the output directory exists and is empty
    assert os.path.exists(output_dir), "Output directory should exist"
    assert os.listdir(output_dir) == [], "Output directory should be empty"

def test_decompress_file_tar_large_file(tmp_path) -> None:
    """
    Test the decompress_file_tar function with a large file.
    """
    # Test case 3: Large file decompression
    compressed_file = tmp_path / "input.tar.gz"
    output_dir = tmp_path / "output"
    data = b"a" * 1000000  # 1 MB of data
    
    # Create a tar-compressed file
    os.makedirs(output_dir)
    input_file = tmp_path / "input.txt"
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with tarfile.open(compressed_file, 'w:gz') as tar:
        tar.add(input_file, arcname="input.txt")
    
    decompress_file_tar(str(compressed_file), str(output_dir))
    
    # Check if the output file exists
    extracted_file = output_dir / "input.txt"
    assert extracted_file.exists(), "Extracted file should exist"
    
    # Read the decompressed data to verify
    with open(extracted_file, 'rb') as f:
        decompressed_data = f.read()
    
    assert decompressed_data == data, "Decompressed data should match the original data"

def test_decompress_file_tar_invalid_input_type(tmp_path) -> None:
    """
    Test the decompress_file_tar function with invalid input file type.
    """
    # Test case 4: Invalid input file type
    output_dir = tmp_path / "output"
    
    with pytest.raises(TypeError):
        decompress_file_tar(123, str(output_dir))  # type: ignore

def test_decompress_file_tar_invalid_output_type(tmp_path) -> None:
    """
    Test the decompress_file_tar function with invalid output directory type.
    """
    # Test case 5: Invalid output directory type
    compressed_file = tmp_path / "input.tar.gz"
    data = b"hello world"
    
    # Create a tar-compressed file
    input_file = tmp_path / "input.txt"
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with tarfile.open(compressed_file, 'w:gz') as tar:
        tar.add(input_file, arcname="input.txt")
    
    with pytest.raises(TypeError):
        decompress_file_tar(str(compressed_file), 123)  # type: ignore

def test_decompress_file_tar_non_existent_input_file(tmp_path) -> None:
    """
    Test the decompress_file_tar function with a non-existent input file.
    """
    # Test case 6: Non-existent input file
    compressed_file = tmp_path / "non_existent.tar.gz"
    output_dir = tmp_path / "output"
    
    with pytest.raises(FileNotFoundError):
        decompress_file_tar(str(compressed_file), str(output_dir))

def test_decompress_file_tar_io_error_on_output_dir(tmp_path) -> None:
    """
    Test the decompress_file_tar function handling of I/O errors on output directory.
    """
    # Test case 7: Handling of I/O errors on output directory
    compressed_file = tmp_path / "input.tar.gz"
    output_dir = tmp_path / "output"
    data = b"hello world"
    
    # Create a tar-compressed file
    input_file = tmp_path / "input.txt"
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with tarfile.open(compressed_file, 'w:gz') as tar:
        tar.add(input_file, arcname="input.txt")
    
    # Simulate an I/O error by making the output directory read-only
    os.makedirs(output_dir)
    os.chmod(output_dir, 0o400)
    
    try:
        with pytest.raises(OSError):
            decompress_file_tar(str(compressed_file), str(output_dir))
    finally:
        # Restore permissions to delete the temporary directory
        os.chmod(output_dir, 0o600)

def test_decompress_file_tar_no_permission_on_input_file(tmp_path) -> None:
    """
    Test the decompress_file_tar function with no permission on input file.
    """
    # Test case 8: No permission on input file
    compressed_file = tmp_path / "input.tar.gz"
    output_dir = tmp_path / "output"
    data = b"hello world"
    
    # Create a tar-compressed file
    input_file = tmp_path / "input.txt"
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with tarfile.open(compressed_file, 'w:gz') as tar:
        tar.add(input_file, arcname="input.txt")
    
    # Remove all permissions from the input file
    os.chmod(compressed_file, 0o000)
    
    try:
        with pytest.raises(OSError):
            decompress_file_tar(str(compressed_file), str(output_dir))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(compressed_file, 0o600)

def test_decompress_file_tar_io_error_on_read_only_output_dir(tmp_path) -> None:
    """
    Test the decompress_file_tar function with read-only output directory.
    """
    # Test case 9: Read-only output directory
    compressed_file = tmp_path / "input.tar.gz"
    output_dir = tmp_path / "output"
    data = b"hello world"
    
    # Create a tar-compressed file
    input_file = tmp_path / "input.txt"
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with tarfile.open(compressed_file, 'w:gz') as tar:
        tar.add(input_file, arcname="input.txt")
    
    os.makedirs(output_dir)
    
    # Simulate a read-only output directory
    os.chmod(output_dir, 0o400)
    
    try:
        with pytest.raises(OSError):
            decompress_file_tar(str(compressed_file), str(output_dir))
    finally:
        # Restore permissions to delete the temporary directory
        os.chmod(output_dir, 0o600)
