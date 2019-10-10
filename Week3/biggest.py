def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    # Your Code Here
    bk = next(iter(aDict.keys()))
    for key in aDict:
        if len(aDict[key]) > len(aDict[bk]):
            bk = key

    return bk
