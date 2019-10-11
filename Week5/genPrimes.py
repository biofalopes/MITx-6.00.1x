"""
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method:
2, 3, 5, 7, 11, ...
 """

# TODO
def genPrimes():
    primes = []
    x = 0
    while True:
        if x % primes[-1] != 0:
            primes.append(x)
            next = x
            yield next


current = genPrimes.next()
print(str(current))
