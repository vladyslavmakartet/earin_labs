import equation

def main() -> None:
    example_function = equation.Function_F(1, 2, 3, 4)
    print("Type:", example_function.get_return_type())
    print("Value for 2:", example_function.get_value(2))

if __name__ == "__main__":
    main()