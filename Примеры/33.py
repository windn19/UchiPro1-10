class Person:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return f'Person: {self.name}'


person = Person('Иван')
print(person.name)
