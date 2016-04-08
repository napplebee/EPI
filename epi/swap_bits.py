# 5.2
import random as rnd


def swap_bits(number, i, j):
    i = 2
    print i, ":",j
    bin_as_arr = [0]*64
    _bin = bin(number)
    idx = 0
    while number > 0:
        bin_as_arr[idx] = number & 1
        number >>= 1
        idx+=1
    original = "".join(map(str, bin_as_arr))
    _ = bin_as_arr[i]
    bin_as_arr[i] = bin_as_arr[j]
    bin_as_arr[j] = _
    swapped = "".join(map(str, bin_as_arr))
    print _bin
    print original
    print swapped
    return original, swapped


def test():
    number = rnd.randint(10, 100000)
    i, j = rnd.randint(0, 63), rnd.randint(0, 63)
    a, b = swap_bits(number, i, j)
    print "Swap bits for {0}".format(number)
    print "Input: {0}, output: {1}".format(a, b)
