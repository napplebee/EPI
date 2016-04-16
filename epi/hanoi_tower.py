# 8.5
# http://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm


def move(n, pegs, source, dest, use):
    if n == 0:
        pegs[dest].append(pegs[source][-1])
        pegs[source].pop()
    elif n > 0:
        transfer(n-1, pegs, source, use, dest)
        pegs[dest].append(pegs[source][-1])
        pegs[source].pop()
        transfer(n-1, pegs, use, dest, source)


def transfer(n, pegs, source, dest, use):
    if n > 0:
        transfer(n-1, pegs, source, use, dest)
        pegs[dest].append(pegs[source][-1])
        pegs[source].pop()
        transfer(n-1, pegs, use, dest, source)


def move_tower_hanoi(n):
    pegs = [list(reversed(range(0, n))), [], []]
    print "Input:"
    print pegs
    move(n, pegs, 0, 1, 2)
    print "Result:"
    print pegs


def test():
    move_tower_hanoi(3)
