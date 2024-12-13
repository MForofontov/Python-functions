import pytest
import os
import tarfile
from compression_functions.files_compression.compress_tar import compress_tar

def test_compress_tar_basic_file_compression(tmp_path) -> None:
    """
    Test the compress_tar function with a single file.
    """
    # Test case 1: Basic file compression
    input_file = tmp_path / "input.txt"
    output_tar = tmp_path / "output.tar.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    compress_tar(str(input_file), str(output_tar))
    
    # Check if the output tar file exists
    assert output_tar.exists(), "Output tar file should exist"
    
    # Extract the tar file to verify
    with tarfile.open(output_tar, 'r:gz') as tar:
        tar.extractall(path=tmp_path)
    
    extracted_file = tmp_path / "input.txt"
    with open(extracted_file, 'rb') as f:
        extracted_data = f.read()
    
    assert extracted_data == data, "Extracted data should match the original data"

def test_compress_tar_empty_directory_compression(tmp_path) -> None:
    """
    Test the compress_tar function with an empty directory.
    """
    # Test case 2: Empty directory compression
    input_dir = tmp_path / "empty_dir"
    output_tar = tmp_path / "output.tar.gz"
    
    os.makedirs(input_dir)
    
    compress_tar(str(input_dir), str(output_tar))
    
    # Check if the output tar file exists
    assert output_tar.exists(), "Output tar file should exist"
    
    # Extract the tar file to verify
    with tarfile.open(output_tar, 'r:gz') as tar:
        tar.extractall(path=tmp_path)
    
    extracted_dir = tmp_path / "empty_dir"
    assert extracted_dir.exists() and extracted_dir.is_dir(), "Extracted directory should exist and be empty"

def test_compress_tar_directory_with_files_compression(tmp_path) -> None:
    """
    Test the compress_tar function with a directory containing files.
    """
    # Test case 3: Directory with files compression
    input_dir = tmp_path / "dir_with_files"
    output_tar = tmp_path / "output.tar.gz"
    data = b"hello world"
    
    os.makedirs(input_dir)
    file1 = input_dir / "file1.txt"
    file2 = input_dir / "file2.txt"
    
    with open(file1, 'wb') as f:
        f.write(data)
    with open(file2, 'wb') as f:
        f.write(data)
    
    compress_tar(str(input_dir), str(output_tar))
    
    # Check if the output tar file exists
    assert output_tar.exists(), "Output tar file should exist"
    
    # Extract the tar file to verify
    with tarfile.open(output_tar, 'r:gz') as tar:
        tar.extractall(path=tmp_path)
    
    extracted_file1 = tmp_path / "dir_with_files" / "file1.txt"
    extracted_file2 = tmp_path / "dir_with_files" / "file2.txt"
    
    with open(extracted_file1, 'rb') as f:
        extracted_data1 = f.read()
    with open(extracted_file2, 'rb') as f:
        extracted_data2 = f.read()
    
    assert extracted_data1 == data, "Extracted data from file1 should match the original data"
    assert extracted_data2 == data, "Extracted data from file2 should match the original data"

def test_compress_tar_invalid_input_path_type(tmp_path) -> None:
    """
    Test the compress_tar function with invalid input path type.
    """
    # Test case 4: Invalid input path type
    output_tar = tmp_path / "output.tar.gz"
    
    with pytest.raises(TypeError):
        compress_tar(123, str(output_tar))  # type: ignore

def test_compress_tar_invalid_output_path_type(tmp_path) -> None:
    """
    Test the compress_tar function with invalid output path type.
    """
    # Test case 5: Invalid output path type
    input_file = tmp_path / "input.txt"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with pytest.raises(TypeError):
        compress_tar(str(input_file), 123)  # type: ignore

def test_compress_tar_non_existent_input_path(tmp_path) -> None:
    """
    Test the compress_tar function with a non-existent input path.
    """
    # Test case 6: Non-existent input path
    input_path = tmp_path / "non_existent"
    output_tar = tmp_path / "output.tar.gz"
    
    with pytest.raises(FileNotFoundError):
        compress_tar(str(input_path), str(output_tar))

def test_compress_tar_io_error_on_output_file(tmp_path) -> None:
    """
    Test the compress_tar function handling of I/O errors on output file.
    """
    # Test case 7: Handling of I/O errors on output file
    input_file = tmp_path / "input.txt"
    output_tar = tmp_path / "output.tar.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    # Simulate an I/O error by making the output directory read-only
    os.chmod(tmp_path, 0o400)
    
    try:
        with pytest.raises(IOError):
            compress_tar(str(input_file), str(output_tar))
    finally:
        # Restore permissions to delete the temporary directory
        os.chmod(tmp_path, 0o700)

def test_compress_tar_no_permission_on_input_file(tmp_path) -> None:
    """
    Test the compress_tar function with no permission on input file.
    """
    # Test case 8: No permission on input file
    input_file = tmp_path / "input.txt"
    output_tar = tmp_path / "output.tar.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    # Remove all permissions from the input file
    os.chmod(input_file, 0o000)
    
    try:
        with pytest.raises(PermissionError):
            compress_tar(str(input_file), str(output_tar))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(input_file, 0o600)

def test_compress_tar_io_error_on_read_only_output_file(tmp_path) -> None:
    """
    Test the compress_tar function with read-only output file.
    """
    # Test case 9: Read-only output file
    input_file = tmp_path / "input.txt"
    output_tar = tmp_path / "output.tar.gz"
    data = b"hello world"
    
    with open(input_file, 'wb') as f:
        f.write(data)
    
    with open(output_tar, 'wb') as f:
        pass
    
    # Simulate a read-only output file
    os.chmod(output_tar, 0o400)
    
    try:
        with pytest.raises(IOError):
            compress_tar(str(input_file), str(output_tar))
    finally:
        # Restore permissions to delete the temporary file
        os.chmod(output_tar, 0o600)
