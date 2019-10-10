def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    # Your Code Here
    count = 0
    for key in aDict:
        for i in aDict[key]:
            count += 1
    return count
