import random
import functools
import time


def timeIt(func):
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsedTime * 1000)))
    return newfunc


@timeIt
def mergeSort(L):
    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1


@timeIt
def selectionSort(L):
    iterations = 0
    for fillslot in range(len(L) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location
        temp = L[fillslot]
        L[fillslot] = L[positionOfMax]
        L[positionOfMax] = temp
        iterations += 1
    print("selectionSort Iterations: " + str(iterations))


@timeIt
def bubbleSort(L):
    iterations = 0
    elem = len(L) - 1
    issorted = False
    while not issorted:
        issorted = True
        for i in range(elem):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                iterations += 1
                issorted = False
    print("bubbleSort Iterations: " + str(iterations))


randomList = random.sample(range(10000), 10000)

mergeSort(randomList.copy())
selectionSort(randomList.copy())
# bubbleSort(randomList.copy())
