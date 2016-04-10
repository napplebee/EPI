# 5.2
import random as rnd


def swap_bits(number, i, j):
    original_bin = bin(number)
    if (number >> i) & 1 == (number >> j) & 1:
        return original_bin, original_bin

    swapped = number ^ ((1 << i) | (1 << j))
    swapped_bin = bin(swapped)
    return original_bin, swapped_bin


def test():
    inp = input("Number (r for random):")
    if inp == "r":
        number = rnd.randint(0, pow(2, 64) - 1)
    else:
        number = int(inp)
    print "Enter swap positions for {0}".format(bin(number))
    i = int(input("i:"))
    j = int(input("j:"))
    original, swapped = swap_bits(number, i, j)

    print "O: {0}".format(original)
    print "S: {0}".format(swapped)
