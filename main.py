def main():
    from bigint import BigInt
    a = BigInt("123")
    b = BigInt("-959")
    c = a.multiply(b)
    print(c)
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
