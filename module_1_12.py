#Объявляю переменную с произвольным текстом
my_string = input('Введите что-нибудь: ')
#Вывожу количество символов введённого текста
print('В Вашей строке ' + str(len(my_string)) + ' символов')
#Вывожу строку my_string в верхнем регистре.
print(str(my_string).upper())
#Вывожу строку my_string в нижнем регистре.
print(str(my_string).lower())
#Вывожу строку my_string, удалив все пробелы.
print(str(my_string).replace(' ', ''))
#Вывожу первый символ строки my_string.
print(str(my_string)[0])
#Вывожу последний символ строки my_string.
print(str(my_string)[-1])