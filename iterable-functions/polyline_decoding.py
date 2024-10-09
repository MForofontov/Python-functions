from typing import List
from decompress_number import decompress_number

def polyline_decoding(text: str) -> List[float]:
    """
    Decode a list of integers compressed with polyline encoding.

    Parameters
    ----------
    text : str
        String representing a compressed list of numbers.

    Returns
    -------
    list
        List with the decoded numbers.
    """
    number_list = []
    index = last_num = 0
    precision = ord(text[index]) - 63
    index += 1
    while index < len(text):
        index, difference = decompress_number(text, index)
        last_num += difference
        number_list.append(last_num)

    return [round(item * (10 ** (-precision)), precision) for item in number_list]