# 6.15


def print_spiral(array):
    x = len(array[0])
    y = len(array)
    max_bounds = {
        "right": x-1,
        "down": y-1,
        "left": 0,
        "up": 1
    }
    number_of_elements = x*y
    coord = (0, -1)
    func = go_right
    result = []
    while number_of_elements > 0:
        number, func, coord = func(array, coord, max_bounds, result)
        number_of_elements -= number
    print(", ".join(map(str, result)))


def go_right(array, coord, maximum, result):
    elements = 0
    increment = 1
    y, x = coord
    x += increment
    while x <= maximum["right"]:
        result.append(array[y][x])
        x += increment
        elements += 1
    maximum["right"] -= 1
    return elements, go_down, (y, x-increment)


def go_down(array, coord, maximum, result):
    elements = 0
    increment = 1
    y, x = coord
    y += increment
    while y <= maximum["down"]:
        result.append(array[y][x])
        y += increment
        elements += 1
    maximum["down"] -= 1
    return elements, go_left, (y-increment, x)


def go_left(array, coord, minimum, result):
    elements = 0
    increment = -1
    y, x = coord
    x += increment
    while x >= minimum["left"]:
        result.append(array[y][x])
        x += increment
        elements += 1
    minimum["left"] += 1
    return elements, go_up, (y, x-increment)


def go_up(array, coord, minimum, result):
    elements = 0
    increment = -1
    y, x = coord
    y += increment
    while y >= minimum["up"]:
        result.append(array[y][x])
        y += increment
        elements += 1
    minimum["up"] += 1
    return elements, go_right, (y-increment, x)


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
