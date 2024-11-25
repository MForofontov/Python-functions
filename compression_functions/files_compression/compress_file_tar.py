import tarfile

def compress_file_tar(input_file: str, output_tar: str) -> None:
    """
    Compress a file using tar with gzip compression.

    Parameters
    ----------
    input_file : str
        The path to the input file to be compressed.
    output_tar : str
        The path to the output tar file to save the compressed data.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during compression.
    """
    try:
        with tarfile.open(output_tar, 'w:gz') as tar:
            tar.add(input_file, arcname=input_file.split('/')[-1])
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during compression: {e}")

