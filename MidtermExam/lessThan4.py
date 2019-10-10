def lessThan4(aList):
    lt4 = []
    for element in aList:
        if len(element) < 4:
            lt4.append(element)
    return lt4
