import zipfile

def decompress_file_zip(input_zip: str, output_dir: str) -> None:
    """
    Decompress a zip-compressed file.

    Parameters
    ----------
    input_zip : str
        The path to the input zip-compressed file.
    output_dir : str
        The path to the output directory to extract the decompressed files.

    Raises
    ------
    TypeError
        If input_zip or output_dir is not a string.
    FileNotFoundError
        If the input zip file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    if not isinstance(input_zip, str):
        raise TypeError("input_zip must be a string")
    if not isinstance(output_dir, str):
        raise TypeError("output_dir must be a string")

    try:
        with zipfile.ZipFile(input_zip, 'r') as zipf:
            zipf.extractall(output_dir)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input zip file {input_zip} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during decompression: {e}")
