class BST(object):
    left = None
    right = None
    value = None
    parent = None

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
        if right is not None:
            right.parent = self
        if left is not None:
            left.parent = self

    def __repr__(self):
        return "[%s]" % self.value

    @staticmethod
    def add(root, value):
        if root is None:
            return BST(value)
        elif value < root.value:
            root.left = BST.add(root.left, value)
        else:
            root.right = BST.add(root.right, value)
        return root

    @staticmethod
    def from_list(l):
        root = BST(l[0])
        for item in l[1:]:
            root = BST.add(root, item)
        return root