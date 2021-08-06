import math


def polysum(n, s):
    """
    n: Number of sides
    s: Length of each side

    returns: sum of the area and square of the perimeter of the regular polygon
    """
    area = (0.25 * n * s * s) / math.tan(math.pi / n)
    perimeter = n * s
    result = area + perimeter ** 2
    return round(result, 4)

