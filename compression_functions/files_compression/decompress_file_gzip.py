import gzip
import shutil
from typing import Any

def decompress_file_gzip(input_gzip: str, output_file: str) -> None:
    """
    Decompress a gzip-compressed file.

    Parameters
    ----------
    input_gzip : str
        The path to the input gzip-compressed file.
    output_file : str
        The path to the output file to save the decompressed data.

    Raises
    ------
    TypeError
        If input_gzip or output_file is not a string.
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    if not isinstance(input_gzip, str):
        raise TypeError("input_gzip must be a string")
    if not isinstance(output_file, str):
        raise TypeError("output_file must be a string")

    try:
        with gzip.open(input_gzip, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_gzip} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during decompression: {e}")
