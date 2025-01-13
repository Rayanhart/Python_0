#На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
# Создаю условие для обнаружения одинаковых чисел
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)