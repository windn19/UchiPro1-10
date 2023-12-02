class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport


person = Person('Иван', 15, '9716234567')
print(person.name)  # Иван
print(person.age)  # 15
print(person.passport)  # 9716234567
