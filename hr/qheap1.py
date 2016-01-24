class MinHeap(object):

    def __init__(self, items):
        self.items = None
        for item in items:
            self.insert(item)

    def count(self):
        return len(self.items)-1

    def insert(self, item):
        self.items.append(item)
        self._sink()

    def delMax(self):
        pass

    def _sink(self, index=None):
        index = 1 if index is None else index

    def _swim(self, index=None):
        index = self.count() if index is None else index


