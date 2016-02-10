def sort(array):
    _internal_sort(array, 0, len(array))


def _internal_sort(array, lo, hi):
    in_place = _partition(array, lo, hi)
    _internal_sort(array, lo, in_place-1)
    _internal_sort(array, in_place+1, hi)


def partition(array, lo, hi):
    pivot = array[lo+(hi-lo)/2]
    i = lo
    j = hi
    while True:
        while array[i] < array[pivot]:
            i += 1
            if i == hi:
                break
        while array[j] > array[pivot]:
            j += 1
            if j == lo:
                break
        if i >= j:
            break
        _swap(array, i, j)
    _swap(array, pivot, j)
    return 1


def _swap(array, i, j):
    buf = array[i]
    array[i] = array[j]
    array[j] = buf
