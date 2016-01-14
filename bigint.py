# 6.9 at page 58
class BigInt(object):

    def __init__(self, string):
        if string[0] == "-":
            self.sign = -1
            stop = 1
        else:
            self.sign = 1
            stop = 0
        self.digits = []
        i = len(string) - 1
        while i >= stop:
            self.digits.append(int(string[i]))
            i -= 1

    def multiply(self, number):
        result = [0]*(len(self.digits)+len(number.digits))
        i = 0
        while i < len(number.digits):
            if number.digits[i] != 0:
                carry = 0
                j = 0
                while j < len(self.digits) or carry:
                    n_digit = int(result[i+j]) + \
                              (int(number.digits[i])*int(self.digits[j]) if j < len(self.digits) else 0) + \
                              carry
                    result[i+j] = n_digit % 10
                    carry = n_digit / 10
                    j += 1
            i += 1
        return BigInt(
                (["-"] if self.sign == -1 or number.sign == -1 else [])+[str(i) for i in reversed(result)]
        )

    # TODO: add sign support
    def __str__(self):
        return "{0}{1}".format(
            "-" if self.sign == -1 else "",
            "".join([str(i) for i in reversed(self.digits)])
        )