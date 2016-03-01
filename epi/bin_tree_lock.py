# 9.4

class Node(object):
    parent = None
    right = None
    left = None
    locked = None
    locked_children = None
    value = None

    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.locked_children = 0
        self.locked = False

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.locked_children != 0 or self.locked:
            raise AssertionError("Already locked!")
        p = self.parent
        while p is not None:
            if p.locked:
                raise AssertionError("Parent is locked")
            p = p.parent
        self.locked = True
        p = self.parent
        while p is not None:
            p.locked_children += 1
            p = p.parent

    def unlock(self):
        self.locked = True
        parent = self.parent
        while parent is not None:
            parent.locked_children -= 1
            parent = parent.parent
