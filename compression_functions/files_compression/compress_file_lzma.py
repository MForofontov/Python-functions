import lzma

def compress_file_lzma(input_file: str, output_lzma: str) -> None:
    """
    Compress a file using lzma.

    Parameters
    ----------
    input_file : str
        The path to the input file to be compressed.
    output_lzma : str
        The path to the output file to save the compressed data.

    Raises
    ------
    TypeError
        If input_file or output_lzma is not a string.
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during compression.
    """
    # Check if input_file and output_lzma are strings
    if not isinstance(input_file, str):
        raise TypeError("input_file must be a string")
    if not isinstance(output_lzma, str):
        raise TypeError("output_lzma must be a string")

    try:
        # Open the input file in binary read mode
        with open(input_file, 'rb') as f_in:
            # Open the output file in binary write mode with lzma compression
            with lzma.open(output_lzma, 'wb') as f_out:
                # Write the contents of the input file to the output file
                f_out.writelines(f_in)
    except FileNotFoundError:
        # Raise a FileNotFoundError if the input file does not exist
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except IOError as e:
        # Raise an IOError if an I/O error occurs during compression
        raise IOError(f"An I/O error occurred during compression: {e}")
