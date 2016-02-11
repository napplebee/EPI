
def main():
    from epi.spiral_array import generate_input
    ar = generate_input(6, 5)
    from epi.spiral_array import print_array
    print_array(ar)
    from epi.spiral_array import print_spiral
    print_spiral(ar)
    print("Cya!")


if __name__ == "__main__":
    main()
