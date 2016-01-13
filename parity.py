def get_parity(input_num):
    bin_num = bin(input_num)
    parity = 0
    while input_num > 0:
        parity ^= 1
        input_num &= input_num - 1
    return bin_num, parity


def test_parity(num):
    bin_num, parity = get_parity(num)
    print("The parity of the {0} ({1}) is: {2}".format(num, bin_num, parity))
