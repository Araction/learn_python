numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(f'Now is {number}')

for i in range(5, 15, 2):
    print(i)

counter = 0
while counter < 10:
    print("I'm here")
    counter = counter + 1

print('Cycle is over')

# letters = [str(let) for let in numbers]
# print(letters)

result = ''
for item in numbers:
    if item != numbers[-1]:
        result = result + str(item) + ", "
    else:
        result = result + str(item)

print(result)

test = [item for item in range(0, 20) if item % 2 == 0]
print(test)

ages = {
    'alex': 18,
    'nick': 20,
    'sara': 16,
    'abram': 34,
    'valentina': 61
}

ages_list = ages.items()
print('It\'s ages_list: ', ages_list)

for name, age in ages_list:
    print(f'{name.capitalize()} is {age} years old')


class String:

    def __init__(self, value):
        self.value = value

    def capitalize(self):
        return self.value[0].upper() + self.value[1:]


name = String('john')
print(name.value)
print(name.capitalize())
