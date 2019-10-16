import timeit


def memoize(function):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function


def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


@memoize
def fib2(n):
    if n < 2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)


t1 = timeit.Timer("fib2(50)", "from __main__ import fib2")
print(t1.timeit(1))


t1 = timeit.Timer("fib1(50)", "from __main__ import fib1")
print(t1.timeit(1))


