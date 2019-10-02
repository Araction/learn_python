
import math
def square(a):

    result = None
    s = a ** 2
    p = a * 4
    d = a * math.sqrt(2)
    tuple(s, p, d)

    return result

side = input("Side A: ")

res = square(side)

print(res)