# 14.7
from epi.models.bst import BST


def create_from_array(array, start, end):
    if start < end:
        mid = start + (end-start) / 2
        value = array[mid]
        return BST(
            value,
            create_from_array(array, start, mid),
            create_from_array(array, mid+1, end)
        )
    else:
        return None


def test():
    n = 10
    l = list(range(0, n))
    root = create_from_array(l, 0, len(l))
    print