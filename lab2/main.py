from bin_vec import BinaryVector


def main():
    a = BinaryVector(127)
    b = BinaryVector(-127)
    print(a)
    print(b)
    g = a.crossover(b, 3)
    print(g)

if __name__ == "__main__":
    main()