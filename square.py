import math


def square(side):
    perimeter = side * 4
    square = side ** 2
    diagonale = side * math.sqrt(2)

    return perimeter, square, diagonale


square_side = int(input("Side: "))
result = square(square_side)
print(f"Perimeter = {result[0]}")
print(f"Square = {result[1]}")
print(f"Diagonale = {result[2]}")

