import random
import functools
import time


def timeIt(func):
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        if not hasattr(newfunc, '_entered'):
            newfunc._entered = True
            startTime = time.time()
            func(*args, **kwargs)
            elapsedTime = time.time() - startTime
            print('function [{}] finished in {} ms'.format(
                func.__name__, int(elapsedTime * 1000)))
            del newfunc._entered
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
    for fillslot in range(len(L) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location
        temp = L[fillslot]
        L[fillslot] = L[positionOfMax]
        L[positionOfMax] = temp


@timeIt
def bubbleSort(L):
    elem = len(L) - 1
    issorted = False
    while not issorted:
        issorted = True
        for i in range(elem):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                issorted = False


randomList = random.sample(range(100000), 100000)

mergeSort(randomList.copy())
selectionSort(randomList.copy())
bubbleSort(randomList.copy())
