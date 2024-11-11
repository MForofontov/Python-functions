def create_whitespace_string(input_string: str) -> str:
    """
    Create a string with the same length as the input string filled with whitespace.

    Parameters
    ----------
    input_string : str
        Input string to get the size from.

    Returns
    -------
    str
        String containing the same number of white spaces as the length of the input string.
    """
    return " " * len(input_string)