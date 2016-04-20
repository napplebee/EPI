
class DistributedArray(object):

    def __init__(self, servers_to_dispatch):
        pass

    def get(self, index):
        pass

    def size(self):
        pass


def find_median():
    ar = DistributedArray()
    median = get_order_stat(ar, ar.size() / 2)