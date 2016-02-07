from hr.qheap1 import MinHeap


def main():
    h = MinHeap()
    h.insert(286789035)
    h.insert(255653921)
    h.insert(274310529)
    h.insert(494521015)
    print(h.get_min())
    h.delete(255653921)
    h.delete(286789035)
    print(h.get_min())
    h.insert(236295092)
    h.insert(254828111)
    h.delete(254828111)
    h.insert(465995753)
    h.insert(85886315)
    h.insert(7959587)
    h.insert(20842598)
    h.delete(7959587)
    print(h.get_min())
    h.insert(-51159108)
    print(h.get_min())
    h.delete(-51159108)
    print(h.get_min())
    h.insert(789534713)
    print("Cya!")


def generate_input():
    import random as rnd
    size = rnd.randint(0, 40)
    result = []
    for _ in range(0, size):
        result.append(rnd.randint(-100, 100))

    return result

if __name__ == "__main__":
    main()
