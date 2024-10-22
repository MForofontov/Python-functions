def expand_tabs(s: str, tabsize: int = 8) -> str:
    """
    Expand tabs in a string to multiple spaces.

    Parameters
    ----------
    s : str
        The input string.
    tabsize : int, optional
        The number of spaces to replace each tab with (default is 8).

    Returns
    -------
    str
        The string with tabs expanded to spaces.

    Examples
    --------
    >>> expand_tabs("hello\tworld")
    'hello   world'
    >>> expand_tabs("hello\tworld", tabsize=4)
    'hello   world'
    """
    return s.expandtabs(tabsize)
