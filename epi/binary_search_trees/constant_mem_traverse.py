from epi.models.bst import BST


def traverse(node):
    if node is None:
        return
    prev = None
    curr = node
    nxt = None
    while curr is not None:
        if prev is None or prev.left == curr or prev.right == curr:
            if curr.left is not None:
                nxt = curr.left
            else:
                print curr.value
                nxt = curr.right if curr.right is not None else curr.parent
        elif curr.left == prev:
            print curr.value
            nxt = curr.right if curr.right is not None else curr.parent
        else: # curr.right == prev
            nxt = curr.parent

        prev = curr
        curr = nxt


def test():
    r = BST(5, BST(1), BST(6, BST(12), BST(55)))

    traverse(r)
    print ""