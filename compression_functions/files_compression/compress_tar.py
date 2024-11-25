import tarfile
import os

def compress_tar(input_path: str, output_tar: str) -> None:
    """
    Compress a file or folder using tar with gzip compression.

    Parameters
    ----------
    input_path : str
        The path to the input file or folder to be compressed.
    output_tar : str
        The path to the output tar file to save the compressed data.

    Raises
    ------
    TypeError
        If input_path or output_tar is not a string.
    FileNotFoundError
        If the input path does not exist.
    IOError
        If an I/O error occurs during compression.
    """
    # Check if input_path and output_tar are strings
    if not isinstance(input_path, str):
        raise TypeError("input_path must be a string")
    if not isinstance(output_tar, str):
        raise TypeError("output_tar must be a string")

    # Check if the input path exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The input path {input_path} does not exist.")

    try:
        # Open the output tar file in write mode with gzip compression
        with tarfile.open(output_tar, 'w:gz') as tar:
            # If the input path is a directory, add the directory and all its contents to the tar file
            if os.path.isdir(input_path):
                tar.add(input_path, arcname=os.path.basename(input_path))
            else:
                # If the input path is a file, add the file to the tar file
                tar.add(input_path, arcname=os.path.basename(input_path))
    except IOError as e:
        # Raise an IOError if an I/O error occurs during compression
        raise IOError(f"An I/O error occurred during compression: {e}")
