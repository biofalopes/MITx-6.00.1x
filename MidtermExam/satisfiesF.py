def f(s):
    return 'a' in s


L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)


def satisfiesF(L):
    for char in L[:]:
        if f(char) == False:
            L.remove(char)
    return len(L)

run_satisfiesF(L, satisfiesF)
