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
    FileNotFoundError
        If the input zip file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    try:
        with zipfile.ZipFile(input_zip, 'r') as zipf:
            zipf.extractall(output_dir)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input zip file {input_zip} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during decompression: {e}")
