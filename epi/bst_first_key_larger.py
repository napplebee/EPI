# 14.5
import random as rnd
from epi.models.bst import BST


def find(current, value):
    node = None
    found = False
    while current is not None:
        if current.value == value:
            found = True
            current = current.right
        elif current.value < value:
            current = current.right
        else:
            node = current
            current = current.left
    return node if found else None


def test():
    # array = [19, 7, 43, 3, 11, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31]
    # key = 32
    n = 17
    array = [rnd.randint(0, n*30) for _ in range(0, n)]
    key = array[3]
    root = BST.from_list(array)
    found_item = find(root, key)
    print "Input:"
    print array
    print "Key:"
    print key
    print "Found item:"
    print found_item
