class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport

    def __getattribute__(self, item):
        if item == 'passport':
            return f'Passport: {self._passport}'
        return object.__getattribute__(self, item)

    def __setattr__(self, item, value):
        if item == 'passport':
            if value.isdigit() and len(value) == 10:
                self._passport = value
            else:
                print('Wrong passport')
                self._passport = '0000000000'
        else:
            object.__setattr__(self, item, value)


person = Person('Иван', 15, '9716234567')
person.passport = 'bad passport'  # Wrong passport
print(person.passport)  # Passport: 0000000000
