import tarfile

def decompress_file_tar(input_tar: str, output_dir: str) -> None:
    """
    Decompress a tar-compressed file.

    Parameters
    ----------
    input_tar : str
        The path to the input tar-compressed file.
    output_dir : str
        The path to the output directory to extract the decompressed files.

    Raises
    ------
    TypeError
        If input_tar or output_dir is not a string.
    FileNotFoundError
        If the input tar file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    # Check if input_tar and output_dir are strings
    if not isinstance(input_tar, str):
        raise TypeError("input_tar must be a string")
    if not isinstance(output_dir, str):
        raise TypeError("output_dir must be a string")

    try:
        # Open the input tar-compressed file in read mode with gzip compression
        with tarfile.open(input_tar, 'r:gz') as tar:
            # Extract all files to the specified output directory
            tar.extractall(path=output_dir)
    except FileNotFoundError:
        # Raise a FileNotFoundError if the input tar file does not exist
        raise FileNotFoundError(f"The input tar file {input_tar} does not exist.")
    except IOError as e:
        # Raise an IOError if an I/O error occurs during decompression
        raise IOError(f"An I/O error occurred during decompression: {e}")
