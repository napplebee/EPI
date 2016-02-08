class MinHeap(object):

    def __init__(self):
        self.items = [None]
        self.count = 0

    def insert(self, item):
        self.items.append(item)
        self.count += 1
        self._swim()

    def get_min(self):
        if self.count == 0:
            return None
        return self.items[1]

    def delete(self, element):
        index = self.items.index(element)

        if index == self.count:
            self.items.pop()
            self.count -= 1
        else:
            self.count -= 1
            self.items[index] = self.items.pop()
            self._sink(index)

    def _sink(self, index=None):
        index = 1 if index is None else index
        while 2*index <= self.count:
            if 2*index+1 <= self.count and self.items[2*index+1] < self.items[2*index]:
                k = 2*index+1
            else:
                k = 2*index
            if self.items[index] < self.items[k]:
                break
            self._swap(index, k)
            index = k

    def _swim(self, index=None):
        index = self.count if index is None else index
        while index > 1 and self.items[index // 2] > self.items[index]:
            self._swap(index, index // 2)
            index //= 2

    def _swap(self, i, j):
        t = self.items[i]
        self.items[i] = self.items[j]
        self.items[j] = t


def main():
    number_of_queries = int(input())
    min_heap = MinHeap()
    while number_of_queries > 0:
        inp = input().split()
        if inp[0] == "1":
            min_heap.insert(int(inp[1]))
        elif inp[0] == "2":
            min_heap.delete(int(inp[1]))
        elif inp[0] == "3":
            print(min_heap.get_min())
        number_of_queries -= 1

if __name__ == "__main__":
    main()
