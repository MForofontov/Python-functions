import tarfile

def compress_file_tar(input_file: str, output_file: str) -> None:
    """
    Compress a file using tar with gzip compression.

    Parameters
    ----------
    input_file : str
        The path to the input file to be compressed.
    output_file : str
        The path to the output tar file to save the compressed data.

    Raises
    ------
    TypeError
        If input_file or output_tar is not a string.
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during compression.
    """
    if not isinstance(input_file, str):
        raise TypeError("input_file must be a string")
    if not isinstance(output_file, str):
        raise TypeError("output_tar must be a string")

    try:
        with tarfile.open(output_file, 'w:gz') as tar:
            tar.add(input_file, arcname=input_file.split('/')[-1])
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during compression: {e}")
