def myLog(x, b):
    if x == b:
        return 1
    elif x < b:
        return 0
    else:
        return 1 + myLog(x / b, b)