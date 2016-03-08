class Problem4(object):
    N = None
    M = None
    items = []
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
        self.M = int(raw_input("M:"))
        for _ in range(0, self.M):
            self.items.append(int(raw_input()))

    def output(self):
        pass


if __name__ == "__main__":
    p = Problem4()
    p.read_input()
    p.output()
