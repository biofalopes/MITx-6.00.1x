def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    # Your code here
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr
    if char == aStr[len(aStr) // 2]:
        return True
    elif char > aStr[len(aStr) // 2]:
        aStr = aStr[len(aStr) // 2:]
        return isIn(char, aStr)
    else:
        aStr = aStr[0:len(aStr) // 2]
        return isIn(char, aStr)
