def equal_pair(word: str, index: int) -> bool:
    """Helper function to check if two consecutive letters at the given index form a double pair."""
    return word[index] == word[index + 1]


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
    # Ensure there's enough length to check three consecutive double pairs
    if len(word) < 6:
        return False

    # Iterate through the string, checking for three consecutive double-letter pairs
    for i in range(0,
                   len(word) - 5,
                   2):  # We go till len(word) - 5 to avoid index out of range
        # Check if three consecutive double pairs exist in the substring starting at index i
        if all(equal_pair(word, i + j)
               for j in range(0, 6, 2)):  # Checks i, i+2, and i+4
            return True  # Return True as soon as we find the triple pair

    return False  # No consecutive double pairs found


inputs = [
    'aabbcc',  #true
    'abccddee0123',  #ture
    'llkkbmm',  #false
    'aaaazz',  #true
    'bbcCdd',  #false
    '0012',  #false
    '001122'  #true
]

for inp in inputs:
    print(trifeca(inp))
