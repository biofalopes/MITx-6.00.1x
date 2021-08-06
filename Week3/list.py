def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def absSq(val):
    return abs(val) ** 2


testList = [1, -4, 8, -9]
# [1, 16, 64, 81]

applyToEach(testList, absSq)

print(testList)

