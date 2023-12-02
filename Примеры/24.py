class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.__passport = passport

    def get_passport(self):
        return f'Passport: {self.__passport}'

    def set_passport(self, passport):
        if passport.isdigit() and len(passport) == 10:
            self.__passport = passport
        else:
            print('Wrong passport')
            self.__passport = '0000000000'

    passport = property(get_passport, set_passport)


person = Person('Иван', 15, '9716234567')
person.passport = 'bad passport'  # Wrong passport
print(person.passport)  # Passport: 0000000000
