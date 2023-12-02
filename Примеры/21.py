class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport

    def get_passport(self):
        return f'Passport: {self.passport}'

    def set_passport(self, passport):
        if passport.isdigit() and len(passport) == 10:
            self.passport = passport
        else:
            print('Wrong passport')
            self.passport = '0000000000'


person = Person('Иван', 15, '9716234567')
person.set_passport('7777777777')
print(person.get_passport())  # Passport: 7777777777
