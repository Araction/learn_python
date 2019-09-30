def arithmetic(number_1, number_2, operator):
    """
    operator should be +, -, * or /.
    """

    result = None

    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            result = 'inf'
    else:
        return f'Unknown operator: {operator}'

    return result


num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))
op = input("Operator: ")

res = arithmetic(num_1, num_2, op)
print(res)
