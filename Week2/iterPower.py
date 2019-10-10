def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    # Your code here
    ans = 1
    while exp > 0:
        ans = ans * base
        exp -= 1
    return ans
