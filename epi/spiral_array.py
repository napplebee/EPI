# 6.15


def print_spiral(array):
    result = list()
    len_y = len(array)-1
    len_x = len(array[0])-1
    number_of_elements = len_x*len_y
    increments = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    inc_index = 0

    index_bounds = [len_x, 0, len_y, 1]
    bound_peeker = 0 # 0 -- straight, 1 -- reverse

    x, y = 0, 0
    inc_x, inc_y = increments[inc_index % 4]
    max_x = index_bounds[bound_peeker % 4]
    max_y = index_bounds[(bound_peeker + 2) % 4]
    while number_of_elements > 0:
        result.append(array[x][y])
        x += inc_x
        y += inc_y
        number_of_elements -= 1
        if x == max_x or y == max_y:
            inc_index += 1
            bound_peeker += 1

            inc_x, inc_y = increments[inc_index % 4]
            max_x = index_bounds[bound_peeker % 4] = index_bounds[bound_peeker % 4] + inc_x
            max_y = index_bounds[(bound_peeker + 2) % 4] = index_bounds[(bound_peeker + 2) % 4] + inc_y
            x, y = y, x

    print(", ".join(result))


def generate_input(n, m):
    import random as rnd
    arr = list()
    for _ in range(0, m):
        l = list()
        for __ in range(0, n):
            l.append(rnd.randint(0, 100))
        arr.append(l)
    return arr


def print_array(array):
    for l in array:
        print(l)
        # print
