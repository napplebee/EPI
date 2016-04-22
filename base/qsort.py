def swap(ar, i, j):
    _ = ar[i]
    ar[i] = ar[j]
    ar[j] = _


def partition(ar, lo, hi):
    pivot = ar[lo]
    i = lo+1
    k = hi
    while True:
        while ar[i] <= pivot: i+= 1
        while ar[k] > pivot: k-= 1
        if i >= k: break
        swap(ar, i, k)
    swap(ar, lo, k)
    return k


def sort(ar, lo, hi):
    if lo >= hi: return
    j = partition(ar, lo, hi)
    sort(ar, lo, j-1)
    sort(ar, j+1, hi)


def qsort(ar):
    sort(ar, 0, len(ar)-1)
