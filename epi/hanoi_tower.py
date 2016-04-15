# 8.5
# http://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm

def transfer(n, pegs, _from, _to, use):
    print "transfer({}, {}, {}, {}, {})".format(n, pegs, _from, _to, use)
    if n > 0:
        transfer(n-1, pegs, _from, use, _to)
        pegs[_to].append(pegs[_from][-1])
        pegs[_from].pop()
        print "Move from peg {0} to peg {1}".format(_from, _to)
        # print pegs
        # print
        transfer(n-1, pegs, use, _to, _from)


def move_tower_hanoi(n):
    pegs = [list(reversed(range(0, n))), [], []]
    print "Input:"
    print pegs
    transfer(n, pegs, 0, 1, 2)
    print "Result:"
    print pegs


def test():
    move_tower_hanoi(3)
