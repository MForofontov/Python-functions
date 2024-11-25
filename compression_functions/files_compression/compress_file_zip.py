import zipfile

def compress_file_zip(input_file: str, output_zip: str) -> None:
    """
    Compress a file using zip.

    Parameters
    ----------
    input_file : str
        The path to the input file to be compressed.
    output_zip : str
        The path to the output zip file to save the compressed data.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during compression.
    """
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(input_file, arcname=input_file.split('/')[-1])
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during compression: {e}")
