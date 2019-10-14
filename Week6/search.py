def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False


def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False


def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)


L1 = []
L2 = [0, 1, 2, 3, 4]
L3 = [0, 1, 2, 3, 4, 5]
e = 5

print("empty list")
print(str(search(L1, e)))
print(str(search3(L1, e)))
print("e is NOT in the list")
print(str(search(L2, e)))
print(str(search3(L2, e)))
print("e is in the list")
print(str(search(L3, e)))
print(str(search3(L3, e)))
