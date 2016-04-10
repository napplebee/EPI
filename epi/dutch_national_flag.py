# 6.1
import random as rnd


def partition(pvt_idx, array):
    smaller = 0
    equal = 0
    greater = len(array)-1
    pivot = array[pvt_idx]
    while equal <= greater:
        if array[equal] < pivot:
            exch(array, equal, smaller)
            smaller += 1
            equal += 1
        elif array[equal] == pivot:
            equal += 1
        else:
            exch(array, equal, greater)
            greater -= 1

    return array


def exch(array, left, right):
    _ = array[left]
    array[left] = array[right]
    array[right] = _


def test():
    n = 10
    array = []
    for _ in range(0, n):
        array.append(rnd.randint(0, n*5))

    print "Generated input:"
    print array
    pivot = input("Pivot idx?")
    if pivot == "":
        pivot = rnd.randint(0, len(array)-1)
    else:
        pivot = int(pivot)
    print "Pivot: {0}".format(array[pivot])
    array = partition(pivot, array)
    print "Result"
    print array
