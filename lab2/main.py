from bin_vec import BinaryVector


def main():
    a = BinaryVector(0)
    b = BinaryVector(-1)
    print(a)
    print(b)
    g = a.random_crossover(b)
    print(g)

if __name__ == "__main__":
    main()