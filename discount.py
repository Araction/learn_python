
def discount(price, discount_percentage):
    if price <= 0:
        print(f"Invalid value")
    elif 1 < discount_percentage < 100:
        print(f"Invalid value")
        cost = price * discount_percentage / 100
    return cost

pr = int(input("Price: "))
disc_percentage = int(input("Discount: "))

result = discount(pr, disc_percentage)
print(result)