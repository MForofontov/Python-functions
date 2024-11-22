import bz2

def compress_file_bz2(input_file: str, output_file: str) -> None:
    """
    Compress a file using bz2.

    Parameters
    ----------
    input_file : str
        The path to the input file to be compressed.
    output_file : str
        The path to the output file to save the compressed data.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during compression.
    """
    try:
        with open(input_file, 'rb') as f_in:
            with bz2.open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during compression: {e}")
