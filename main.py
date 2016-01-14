from parity import test_parity
from robot import prove, get_battery_capacity


def main():
    for i in range(0, 1000000):
        steps = generate_input()
        prove(get_battery_capacity(steps), steps)
    print("Cya!")


def generate_input():
    import random as rnd
    size = rnd.randint(0, 40)
    result = []
    for _ in range(0, size):
        result.append(rnd.randint(-100, 100))

    return result

if __name__ == "__main__":
    main()
