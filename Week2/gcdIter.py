def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    # Your code here
    if a > b:
        result = b
    else:
        result = a

    while (a % result) != 0 or (b % result) != 0:
        result -= 1

    return result
