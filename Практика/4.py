class Password:
    def set_password(self):
        print('Введите пароль')
        password1 = input()
        print('Введите пароль еще раз')
        password2 = input()
        if password1 == password2:
            self.__password = password1
            print('Пароль установлен')
        else:
            print('Ошибка')

    def change_password(self):
        print('Введите старый пароль')
        password = input()
        print('Введите новый пароль')
        password_new = input()
        if password == self.__password:
            self.__password = password_new
            print('Пароль изменен')
        else:
            print('Ошибка')

    def __getattr__(self, item):
        if item == 'password':
            print('Нет доступа')
        else:
            return super().__getattribute__()


# [p := Password(), p.set_password(), p.password, p.change_password(), p.change_password()]
eval(input())
