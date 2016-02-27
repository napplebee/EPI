import random as rnd

class NumberStorageNde(object):
    storage = []

    def __init__(self, size, index=0):
        self.index = index
        self.size = size
        for _ in range(0, size):
            self.storage.append(rnd.randint(0, size*2))

    def next(self):
        element = self.storage[self.index]
        self.index += 1
        return element



def median():
    heap = Heap()
