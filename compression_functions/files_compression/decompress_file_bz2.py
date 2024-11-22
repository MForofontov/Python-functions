import bz2

def decompress_file_bz2(input_file: str, output_file: str) -> None:
    """
    Decompress a bz2-compressed file.

    Parameters
    ----------
    input_file : str
        The path to the input bz2-compressed file.
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
        with bz2.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during decompression: {e}")
