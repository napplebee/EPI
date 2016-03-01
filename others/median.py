import random as rnd


class Heap(object):
    pass


class NumberStorageNde(object):
    storage = []

    def __init__(self, size, index=0):
        self.index = index
        self.size = size
        # just want to have number in order
        seed = rnd.randint(0, size*2)
        for i in range(0, size):
            self.storage.append(seed+i)

    def next(self):
        element = self.storage[self.index]
        self.index += 1
        return element, self.index



def median():
    storage_nodes = []
    number_of_nodes = 10
    for i in range(0, 10):
        heap = Heap()
