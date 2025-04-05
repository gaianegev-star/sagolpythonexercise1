# def equal_pair(word: str, index: int) -> bool:
#     """Helper function to check if two consecutive letters at the given index form a double pair."""
#     return word[index] == word[index + 1]


def trifeca(word: str) -> bool:
    """Checks whether word contains three consecutive double-letter pairs.

    Parameters
    ----------
    word : string
        Input to check

    Returns
    -------
    result : bool
        True if three consecutive double-letter pairs were found,
        False otherwise
    """
    # Ensure there's enough length to contain three consecutive double pairs (6 characters)
    if len(word) < 6:
        return False

    for i in range(0, len(word) - 5):  # range limited to len(word) - 5 to avoid index out of range
        if all(word[i+j] == word[i+j+1]
               for j in range(0, 6, 2)):  # Checks identical pairs for i, i+2, and i+4
            return True  

    return False  
