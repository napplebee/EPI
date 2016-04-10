# 5.5
import random as rnd


def powerset(items):
    elements = list(items)
    r = []
    bit_masks = range(0, pow(2, len(elements)))
    for mask in bit_masks:
        subset = []
        shift = 0
        while mask > 0:
            extr = 1 << shift
            if mask & extr > 0:
                subset.append(elements[shift])
                mask ^= extr
            shift += 1
        r.append(subset)
    return r


def test():
    n = 30
    input_list = set()
    for _ in range(0, n):
        input_list.add(rnd.randint(0, n*10))

    print "Input:"
    print input_list
    result = powerset(input_list)
    print result
