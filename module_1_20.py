print('----------Словари----------')

# Создаю переменную my_dict и присваиваю ей словарь из нескольких пар ключ-значение
my_dict = {'Misha':89652349875, 'Lena':89864657656, 'Igor':89474568348}
print('Dict:', my_dict)
# Вывожу на экран одно значение по существующему ключу
print('Existing value:', my_dict['Lena'])
# И одно по отсутствующему из словаря
my_dict['Ivan'] = 89456547345
print('Not existing value:', my_dict['Ivan'])
# Добавляю ещё две пары того же формата в словарь
my_dict.update({'Karina':89674567849, 'Frosya':89578764567})
# Удаляю одну из пар в словаре по существующему ключу из словаря
# и вывожу значение из этой пары на экран
a = my_dict.pop('Misha')
print('Deleted value:', a)
# Вывожу на экран словарь my_dict
print('Modified dictionary:', my_dict)

print('---------Множества---------')

# Создаю переменную my_set и присваиваю ей множество,
# состоящее из разных типов данных с повторяющимися значениями
my_set = {2, 2, True, True, 5, 5, 5, 'Hello', 'Hello'}
print('Set:', my_set)
# Добавляю 2 новых элемента в множество my_set
my_set.add(45346)
my_set.add('2025')
# Удаляю один элемент из множества my_set
my_set.remove(5)
print('Modified set:', my_set)