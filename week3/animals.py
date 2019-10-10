animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}


def how_many(aDict):
    count = 0
    for key in aDict:
        for i in aDict[key]:
            count += 1
    return count


def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    bk = next(iter(aDict.keys()))
    for key in aDict:
        if len(aDict[key]) > len(aDict[bk]):
            bk = key

    return bk


print(biggest(animals))
