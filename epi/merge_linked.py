# 7.1


class Node(object):
    nxt = None
    value = None

    def __init__(self, value, n=None):
        self.nxt = n
        self.value = value


def merge(head1, head2):

    if head1.value < head2.value:
        result = head1
        current = result
        head1 = head1.nxt
    else:
        result = head2
        current = result
        head2 = head2.nxt

    while head1 is not None or head2 is not None:
        if head2 is None:
            current.nxt = head1
            head1 = head1.nxt
        elif head1 is None:
            current.nxt = head2
            head2 = head2.nxt
        elif head1.value > head2.value:
            current.nxt = head2
            head2 = head2.nxt
        else:
            current.nxt = head1
            head1 = head1.nxt

        current = current.nxt

    return result


def test():
    head1 = Node(1, Node(2, Node(4, Node(9, Node(10)))))
    head2 = Node(3, Node(5, Node(8)))
    merged = merge(head1, head2)
    result = ""
    while merged is not None:
        result = "{0}({1})->".format(result, merged.value)
        merged = merged.nxt
    print result
