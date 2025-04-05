
def is_palindrome(input: str) -> bool:
    """Checks if a specific input is a palindrome 

    Parameters 
    ----------
    input : string
        Input to check if is a palindrome

    Returns
    -------
    result : bool 
        True if the input is a palindrome

    """
    result = False
    if input == input[::-1]:
        result = True
    return result


def check_palindrome():
    """Runs through all 6-digit numbers and checks the mentioned conditions.

    The function prints out the numbers that satisfy this condition.

    Notes
    -----
    It should print out the first number (with a palindrome in its last 4 digits),not all four "versions" of it.
    """
    result = []
    for i in range(100000, 1000000):
        if (is_palindrome(str(i)[-4:]) and is_palindrome(str(i + 1)[-5:])
             and is_palindrome(str(i + 2)[1:-1]) and  is_palindrome(str(i + 3))):
            result.append(i)   

    print(result)