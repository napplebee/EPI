def merge(ar, lo, mid, hi):
    aux = ar[:]
    i = lo
    j = mid + 1
    k = lo
    while k <= hi:
        if i > mid:
            ar[k] = aux[j]
            j += 1
        elif j > hi:
            ar[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            ar[k] = aux[i]
            i += 1
        else:
            ar[k] = aux[j]
            j += 1
        k += 1
    return ar


def sort(ar, lo, hi):
    if hi <= lo: return
    mid = lo + (hi - lo) / 2
    sort(ar, lo, mid)
    sort(ar, mid+1, hi)
    merge(ar, lo, mid, hi)


def top_down_merge_sort(ar):
    sort(ar, 0, len(ar)-1)


def bottom_up_merge_sort(ar):
    n = len(ar)
    sz = 1
    while sz < n:
        lo = 0
        while lo < n - sz:
            merge(ar, lo, lo + sz - 1, min(lo+sz+sz - 1, n - 1))
            lo += sz + sz
        sz = sz + sz
