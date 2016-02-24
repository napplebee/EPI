# 9.3


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def is_symmetric(node):
    left = []
    collect_left(node.left, left)
    right = []
    collect_right(node.right, right)
    return "".join(map(str, left)) == "".join(map(str, right))


def collect_left(node, result):
    result.append(node.value)
    if node.left is not None:
        collect_left(node.left, result)
    if node.right is not None:
        collect_left(node.right, result)
    return result


def collect_right(node, result):
    result.append(node.value)
    if node.right is not None:
        collect_right(node.right, result)
    if node.left is not None:
        collect_right(node.left, result)
    return result


def test():
    root = Node(0, Node(1, Node(2, Node(3), Node(5))), Node(1, None, Node(2, Node(5), Node(3))))
    print(is_symmetric(root))
