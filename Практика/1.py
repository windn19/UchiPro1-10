# Напиши программу, в которой создай класс Student. Реализуй в классе следующие методы:
#     • __init__(name, course) — добавляет объекту атрибуты name — строка и course — целое число от 5 до 11,
#     status со значением student.
#     • next_course() — увеличивает course на единицу, пока студент не закончит обучение
#     (11 класс — последний год обучения). Если после вызова метода next_course, класс становится больше 11,
#     то значение атрибута course устанавливается на None, a status на строку graduate.
#     • deduction() — изменяет значение атрибута course на None, a status на строку expelled.
#     • get_info() — возвращает строку вида «Student: {name} ({course}), status: {status}», например,
#     «Student: Иванов Иван Иванович (None), status: expelled».
#
# При решении задачи используй инкапсуляцию, ограничь прямой доступ к атрибутам. Считай с клавиатуры 3 строки.
# На первой строке указано значение атрибута name, на второй строке целое число — course, на третьей строке название
# метода: next_course или deduction. Создай экземпляр класса с этими параметрами и выполни метод, который был указан
# в третьей строке. Выведи результат метода get_info() данного объекта после выполнения метода.
#
# Входные данные:
# Три строки — name, одно целое число — course и строка с названием метода.
# Выходные данные:
# Выводится строка.
#
# Пример работы программы:
# student1 = Student('Михайлов Петр', 10)
# print(student1.get_info())
# student1.next_course()
# student1.next_course()
# print(student1.get_info())
# student2 = Student('Васильев Сергей', 5)
# print(student2.get_info())
# student2.deduction()
# print(student2.get_info())
# Вывод:
# Student: Михайлов Петр (10), status: student
# Student: Михайлов Петр (None), status: graduate
# Student: Васильев Сергей (5), status: student
# Student: Васильев Сергей (None), status: expelled

# Пример ввода:
# Иванов Иван Иванович
# 11
# next_course
# Пример вывода:
# Student: Иванов Иван Иванович (None), status: graduate

class Student:
    def __init__(self, name, course):
        self.__name = name
        self.__status = 'student'
        self.__course = course

    def next_course(self):
        """Перевод на следующий год."""
        if self.__course <= 10:
            self.__course += 1
        else:
            self.__course = None
            self.__status = 'graduate'

    def deduction(self):
        """Отчисление."""
        self.__course = None
        self.__status = 'expelled'

    def get_info(self):
        """Получение информации."""
        return f'Student: {self.__name} ({self.__course}), status: {self.__status}'


for line in range(int(input())):
    eval(input())

# student1 = Student('Михайлов Петр', 10)
# print(student1.get_info())
# student1.next_course()
# student1.next_course()
# print(student1.get_info())
# student2 = Student('Васильев Сергей', 5)
# print(student2.get_info())
# student2.deduction()
# print(student2.get_info())

