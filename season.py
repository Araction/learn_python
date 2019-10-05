
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
    # Here process error when getting user's value
    month = int(input("Input month number: "))
except ValueError:
    # Print message if the error has happen
    print("Please, input integer values")
else:
    # Here exec our function with passing args if all ok
    result = season(month)
    print(result)
finally:
    # Here print will anyway
    print("Program is over")
