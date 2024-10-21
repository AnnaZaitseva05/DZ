# Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(2, 'столбец')
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параментров:

values_list = [1, 'строка', True]
values_dict = {'a':1, 'b':'строка', 'c':True}

def print_params(*args, **kwargs):
    print(args)
    print(kwargs)

print_params(*values_list, **values_dict)

# Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
