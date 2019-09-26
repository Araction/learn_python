# +, -, *, /, **
# int, float


counter = 0
small_rabbits = 3
big_rabbits = 6
cages = 4


rabbits = small_rabbits + big_rabbits
print(f'All rabbits count: {rabbits}')
print('All rabbits count: ' + str(rabbits) + 'jhbksdbf' + str(counter))
rabbits_per_cage = rabbits / cages
print('Rabbits per cage: {}, foo bar bar hello world {}'.format(
    rabbits_per_cage, counter
))
rabbits_per_cage = int(rabbits_per_cage)
print('Rabbits per cage (old) %i-%i' % (rabbits_per_cage, counter))

print(4**2)

yesterdays_todo_list = ['study']
todays_todo_list = ['cooking', 'cleaning']

todos = yesterdays_todo_list + todays_todo_list

print(todos)

result = None
bound = 10

x = int(input('Input X: '))
y = int(input('Input Y: '))

if not x:
    x = 1
if not y:
    y = 1

sum_xy = x + y

dict_w = {
    'first': 1,
    'second': 2,
    'result': 'Yes, sum is less than 10' if sum_xy < bound else 'Not, sum is more than 10 or equal'
}

if sum_xy < bound:
    result = 'Yes, sum is less than 10'
else:
    result = 'Not, sum is more than 10 or equal'


print(result)


