def complicated_palindrome():
    """Runs through all 6-digit numbers and checks the mentioned conditions.

    The function prints out the numbers that satisfy this condition.

    Notes
    -----
    It should print out the first number (with a palindrome in its last 4 digits),not all four "versions" of it.
    """
    result = []
    for i in range(100000, 1000000):
        if is_palindrome(str(i)[-4:]) and is_palindrome(str(i + 1)[-5:]) and is_palindrome(str(i + 2)[1:-1]) and  is_palindrome(str(i + 3)):
            result.append(i)   

    print(result)




def is_palindrome(int) -> bool:
    """Runs through string and checks if they are palindroms.

    Inputs:
    int: 

    """
    result = False
    if int == int[::-1]:
        result = True
    return result
