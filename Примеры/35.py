class Person:
    __slots__ = ('name', 'age', 'passport')

    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport


person = Person('Иван', 15, '9716234567')
person.course = 1  # Ошибка AttributeError: 'Person' object has no attribute 'course'
