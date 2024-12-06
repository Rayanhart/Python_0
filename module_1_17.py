# Создаю переменную типа кортеж из нескольких элементов разных типов данных
immutable_var = 2, 'string', False, [2, 3, 4]
print(immutable_var)
# Пытаюсь изменить элементы кортежа, но выдает ошибку из-за того, что элементы
# кортежа не меняются, если они сами по себе не меняемые
#immutable_var [0] = 2
immutable_var [3][2] = 2
print(immutable_var)
# Создаю переменную типа список из нескольких элементов, в отличие от кортежа,
# его элементы можно сводно менять
mutable_list = [32, '"Hello World"', True]
mutable_list[0] = 45
mutable_list[1] = mutable_list[1][::-1]
mutable_list[2] = False
print(mutable_list)