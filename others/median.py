
class DistributedArray(object):
    """
    Dummies implementation just to give an idea
    """
    srvs = None
    _size = 0

    def __init__(self, servers_to_dispatch):
        self.srvs = servers_to_dispatch
        self._size = sum([len(i) for i in servers_to_dispatch])

    def get_item(self, index):
        i = 0
        while index - len(self.srvs[i]) >= 0:
            index -= len(self.srvs[i])
            i = i+1

        return self.srvs[i][index]

    def size(self):
        return self._size

    def swap(self, i, j):
        srv_idx1 = 0
        while i - len(self.srvs[srv_idx1]) >= 0:
            i -= len(self.srvs[srv_idx1])
            srv_idx1 += 1

        srv_idx2 = 0
        while j - len(self.srvs[srv_idx2]) >= 0:
            j -= len(self.srvs[srv_idx2])
            srv_idx2 += 1
        _ = self.srvs[srv_idx1][i]
        self.srvs[srv_idx1][i] = self.srvs[srv_idx2][j]
        self.srvs[srv_idx2][j] = _

    def __repr__(self):
        s = []
        for srv in self.srvs:
            s.append(", ".join(map(str, srv)))
        return "[{0}]".format(", ".join(s))

def partition(ar, lo, hi):
    pivot = ar.get_item(lo)
    i = lo+1
    j = hi
    while True:
        while ar.get_item(i) <= pivot and i < hi:
            i += 1
            if i == hi: break
        while ar.get_item(j) > pivot and j > lo:
            j -= 1
            if j == lo: break
        if i >= j: break
        ar.swap(i, j)
    ar.swap(lo, j)
    return j

def get_order_stat(ar, kth, lo, hi):
    j = partition(ar, lo, hi)
    if j == kth:
        return ar.get_item(j)
    elif j > kth:
        return get_order_stat(ar, kth, lo, j-1)
    else: # j < kth
        return get_order_stat(ar, kth - j, j+1, hi)


def find_median(ar):
    median = get_order_stat(ar, (ar.size()-1) / 2, 0, ar.size()-1)
    return median


def test():
    import random as rnd
    n = 10
    for n in range(1, 100):
        ar = DistributedArray([
            [rnd.randint(0, n*100) for _ in range(0, n)],
            [rnd.randint(0, n*100) for _ in range(0, n)]
        ])
        print ar
        m = find_median(ar)
        print m