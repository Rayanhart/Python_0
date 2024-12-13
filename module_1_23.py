# На вход мне поступают список оценок grades и множество имен студентов students
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Создаю список средних оценок av_grades
av_grades = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
# Перевожу множество students в список
students = list(students)
# Сортирую список students в алфавитном порядке
students = sorted(students)
# Создаю словарь av_score в котором как ключи указываю имена студентов,
# а в значения, их средние оценки
av_score = {students[0]:av_grades[0], students[1]:av_grades[1], students[2]:av_grades[2], students[3]:av_grades[3], students[4]:av_grades[4]}
print(av_score)