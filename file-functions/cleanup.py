import os 
import shutil
from typing import List

def cleanup(directory: str, exclude: List[str]) -> None:
    """
    Clean up a directory by removing all files and subdirectories except those specified in the exclusion list.

    Parameters
    ----------
    directory : str
        The path to the directory to clean up.
    exclude : List[str]
        A list of filenames or subdirectory names to exclude from removal.

    Returns
    -------
    None
    """
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if item not in exclude:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)