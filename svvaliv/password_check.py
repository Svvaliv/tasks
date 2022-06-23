# Класс имитирует регистрацию пользователей с проверкой валидности логина и пароля

from string import digits, ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digits(value):
        "Проверяем, содержаться ли цифры в пароле"
        for digit in digits:
            if digit in value:
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        "Проверяем, содержаться ли буквы в верхнем и нижнем регистре в пароле"
        count_lower = 0
        count_upper = 0
        for symbol in value:
            if symbol.islower():
                count_lower += 1
            elif symbol.isupper():
                count_upper += 1
        if count_upper and count_lower:
            return True
        return False

    @staticmethod
    def is_include_only_latin(value):
        "Проверяем, что пароль содержит только латинские буквы"
        for letter in value:
            if letter.isalpha() and letter not in ascii_letters:
                return False
        return True

    @staticmethod
    def check_password_dictionary(value):
        "Проверяем, не находиться ли пароль в хранилище простых паролей"
        with open('easy_passwords.txt', encoding='utf-8') as easy:
            for i in easy.readlines():
                if value == i.strip():
                    return False
        return True

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if value.count('@') != 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if value.count('.') != 1:
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if not (4 < len(value) < 12):
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digits(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 43  # raise TypeError("Пароль должен быть строкой")
