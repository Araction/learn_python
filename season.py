
def season(month_number):
    if not 1 < month_number < 13:
        return f"Invalid month number: {month_number}"

    if month_number in (12, 1, 2):
        return "It's winter"
    if month_number in (3, 4, 5):
        return "It's spring"
    if month_number in (6, 7, 8):
        return "It's summer"
    if month_number in (9, 10, 11):
        return "It's autumn"


try:
    month = int(input("Input month number: "))
except ValueError:
    print("Please, input integer values")
else:
    result = season(month)
    print(result)
finally:
    print("Program is over")
