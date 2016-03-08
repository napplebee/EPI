class Problem4(object):
    N = None
    items = []
    result = 0 # default output
    """
    Sum of 2 numbers in an array
    Identify whether there exists a pair of numbers in an array such that their sum is equal to N.

    Input:
    The first line contains one integer N, which is the sum we are trying to find
    The second line contains one integer M, which is length of the array
    This is followed by M lines each containing one element of the array.

    Output:
    Output 1 if there exists a pair of numbers in the array such that their sum equals N. If such a pair does not exist, output 0.
    """

    def read_input(self):
        self.N = int(raw_input("N:"))
        M = int(raw_input("M:"))
        for _ in range(0, M):
            self.items.append(int(raw_input()))

    def output(self):
        self.naive_impl()
        print self.result

    def naive_impl(self):
        i = 0
        l = len(self.items)
        while i <= l - 2:
            num = self.N - self.items[i]
            k = i+1
            while k <= i - 1:
                if self.items[k] == num:
                    self.result = 1
                    return
                k += 1
            i += 1


def test():
    p = Problem4()
    p.read_input()
    p.output()
