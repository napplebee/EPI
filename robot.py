def get_battery_capacity(steps):
    # steps:
    # [3, 10, -10, -20, 15]
    # [-10, 1, -15, 3, -10, -12, 5, 5]
    capacity = 0
    energy_needed = False
    for step in steps:
        pass


# todo: check for optimum
def prove(max_capacity, steps):
    current_capacity = max_capacity
    for step in steps:
        print("Step: {0}".format(step))
        current_capacity += step
        if current_capacity > max_capacity:
            current_capacity = max_capacity
        if current_capacity < 0:
            print("ERROR: Current capacity below zero")
            return
        print("Current capacity: {0}".format(current_capacity))
