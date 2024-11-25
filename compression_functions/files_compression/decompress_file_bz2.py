import bz2

def decompress_file_bz2(input_bz2: str, output_file: str) -> None:
    """
    Decompress a bz2-compressed file.

    Parameters
    ----------
    input_bz2 : str
        The path to the input bz2-compressed file.
    output_file : str
        The path to the output file to save the decompressed data.

    Raises
    ------
    TypeError
        If input_bz2 or output_file is not a string.
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    if not isinstance(input_bz2, str):
        raise TypeError("input_bz2 must be a string")
    if not isinstance(output_file, str):
        raise TypeError("output_file must be a string")

    try:
        with bz2.open(input_bz2, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
    except FileNotFoundError:
        raise FileNotFoundError(f"The input file {input_bz2} does not exist.")
    except IOError as e:
        raise IOError(f"An I/O error occurred during decompression: {e}")
