# 6.22
mapping = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}


def get_mnemonics_recursive(ph_num, mnemonic):
    if len(ph_num) == 0:
        print mnemonic
        return
    digit = ph_num[0]
    for letter in mapping[digit]:
        m = mnemonic + letter
        get_mnemonics_recursive(ph_num[1:], m)


def test():
    ph_num = [2, 3, 2]
    get_mnemonics_recursive(ph_num, "")
