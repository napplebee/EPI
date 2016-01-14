# 6.3
def get_battery_capacity(steps):
    result_capacity = 0
    current_capacity = 0
    energy_needed = False
    for step in reversed(steps):
        # just skip last positive elements
        if not energy_needed:
            if step < 0:
                energy_needed = True
            else:
                continue
        current_capacity -= step
        if current_capacity > result_capacity:
            result_capacity = current_capacity
        elif current_capacity < 0:
            current_capacity = 0

    return result_capacity


def prove(max_capacity, steps):
    print("Testing assumption: {0} for {1}.".format(max_capacity, steps))
    current_capacity = max_capacity
    for step in steps:
        print("Step: {0}".format(step))
        current_capacity += step
        if current_capacity > max_capacity:
            current_capacity = max_capacity
        if current_capacity < 0:
            print("ERROR: Current capacity below zero")
            with open("result.out", "w+") as f:
                f.write("Error found for the assumption: {0} for {1}.".format(max_capacity, steps))
                import os
                f.write(os.linesep)
            return
        print("Current capacity: {0}".format(current_capacity))

    print("Assumption is correct")
