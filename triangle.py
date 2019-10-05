import math


def triangle(side):
    square = math.sqrt(3) / 4 * side ** 2
    perimeter = side * 3
    height = math.sqrt(3) / 2 * side
    out_circle_radius = side / math.sqrt(3)
    in_circle_radius = side / 2 * math.sqrt(3)

    return square, perimeter, height, out_circle_radius, in_circle_radius


try:
    triangle_side = int(input("Triangle Side: "))
except ValueError:
    print("Please, only integer numbers")
else:
    result = triangle(triangle_side)

    print(f"Square = {result[0]}")
    print(f"Perimeter = {result[1]}")
    print(f"Height = {result[2]}")
    print(f"Out circle radius = {result[3]}")
    print(f"In circle radius = {result[4]}")
