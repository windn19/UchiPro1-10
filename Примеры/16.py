class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport


person = Person('Иван', 15, '9716234567')
print(person.name)  # Иван
print(person._age)  # 15
print(person.__passport)  # Ошибка AttributeError
