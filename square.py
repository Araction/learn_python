import math


def square(side):
    perimeter = side * 4
    square = side ** 2
    diagonale = side * math.sqrt(2)

    return perimeter, square, diagonale


# Here getting value from user to square_side variable
square_side = input("Side: ")

# Here convert string value to integer of square_side variable
square_side = int(square_side)

# Here exec our function with passing args
result = square(square_side)

# Here print gotten values
print(f"Perimeter = {result[0]}")
print(f"Square = {result[1]}")
print(f"Diagonale = {result[2]}")
