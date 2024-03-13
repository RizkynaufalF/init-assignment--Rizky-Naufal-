def type_triangle(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or x == z or y == z:
        return "Isosceles triangle"
    else:
        return "Any triangle"


def main():
    x = int(input("Enter the side length x: "))
    y = int(input("Enter the side length y: "))
    z = int(input("Enter the side length z: "))

    type = type_triangle(x, y, z)
    print("The included triangle is:", type)


if __name__ == "__main__":
    main()
