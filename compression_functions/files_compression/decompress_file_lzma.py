import lzma

def decompress_file_lzma(input_file: str, output_file: str) -> None:
    """
    Decompress an lzma-compressed file.

    Parameters
    ----------
    input_file : str
        The path to the input lzma-compressed file.
    output_file : str
        The path to the output file to save the decompressed data.

    Raises
    ------
    TypeError
        If input_file or output_file is not a string.
    FileNotFoundError
        If the input file does not exist.
    IOError
        If an I/O error occurs during decompression.
    """
    # Check if input_file and output_file are strings
    if not isinstance(input_file, str):
        raise TypeError("input_file must be a string")
    if not isinstance(output_file, str):
        raise TypeError("output_file must be a string")

    try:
        # Open the input file in binary read mode with lzma decompression
        with lzma.open(input_file, 'rb') as f_in:
            # Open the output file in binary write mode
            with open(output_file, 'wb') as f_out:
                # Write the contents of the input file to the output file
                f_out.writelines(f_in)
    except FileNotFoundError:
        # Raise a FileNotFoundError if the input file does not exist
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    except OSError as e:
        # Raise an IOError if an I/O error occurs during decompression
        raise OSError(f"An I/O error occurred during decompression: {e}")
