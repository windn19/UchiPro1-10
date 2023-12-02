class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport

    def get_passport(self):
        return f'Passport: {self._passport}'

    def set_passport(self, passport):
        if passport.isdigit() and len(passport) == 10:
            self._passport = passport
        else:
            print('Wrong passport')
            self._passport = '0000000000'

    passport = property(get_passport, set_passport)


person = Person('Иван', 15, 'bad passport')
print(person.passport)
