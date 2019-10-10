def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    # Your code here
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcdRecur(min(a, b), max(a, b) % min(a, b))
