
int_var = 1  # int
float_var = 1.0  # float
str_var = 'some string'

int_list_var = [1, 2, 3]
float_list_var = 1.0, 2.0
multi_types_list_var = [1, 2.0, 'string']
multi_types_list_var.append(1234)

tuple_var = (1, 2, 3)

dict_var = {
    'test_int': 1,
    'test_float': 1.0,
    'test_list': [],
    'test_dict': {}
}

dict_var_2 = dict(
    test_int=1,
    test_float=2.0
)

site_map = {
    'about': 'About Page',
    'help': 'Help Page',
    'home': 'Home Page'
}

result = ''
for key, val in site_map.items():
    result += f'<a href="https://some.com/{key}/">{val}</a>\n'

print(result)
