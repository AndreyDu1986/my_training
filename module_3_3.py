def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 30)
print_params(c = [1, 2, 3])
print_params([1, 2], ['str'], [5, 6])
print_params(' ', ' ', ' ')

values_list = [100, 'разные типы', False]
values_dict = {'a': 200, 'b': 'словарь', 'c': [1, 2, 3]}
print_params(*values_list)
print(values_dict)
print_params(*values_dict)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)