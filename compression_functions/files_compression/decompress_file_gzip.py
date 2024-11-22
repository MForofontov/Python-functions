import gzip
import shutil

def decompress_file_gzip(input_file: str, output_file: str) -> None:
    """
    Decompress a gzip-compressed file.

    Parameters
    ----------
    input_file : str
        The path to the input gzip-compressed file.
    output_file : str
        The path to the output file to save the decompressed data.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    try:
        with gzip.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during decompression: {e}")
