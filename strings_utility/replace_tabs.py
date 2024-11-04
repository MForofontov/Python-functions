def replace_tabs(s: str, tabsize: int = 4) -> str:
    """
    Replaces tabs in a string to multiple spaces.

    Parameters
    ----------
    s : str
        The input string.
    tabsize : int, optional
        The number of spaces to replace each tab with (default is 8).

    Returns
    -------
    str
        The string with tabs replaced to spaces.

    Examples
    --------
    >>> expand_tabs("hello\tworld")
    'hello   world'
    >>> expand_tabs("hello\tworld", tabsize=4)
    'hello   world'
    """
    if not isinstance(s, str):
        raise TypeError("The input must be a string.")
    if tabsize < 0:
        raise ValueError("Tab size must be non-negative.")
    return s.replace("\t", " " * tabsize)
