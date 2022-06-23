# Генератор паролей. Пароли должны содержать хотя бы одну цифру и хотя бы одна заглавную букву.
# А так же не должны содержать заведомо похожих символов из набора "0Oo1Il"

from random import sample
from string import ascii_letters, digits

letter = ''.join((set(set(ascii_letters) | set(digits)) - set(
    '0Oo1Il')))  # Создаём строку символов, из которой будут генерироваться пароли


def generate_password(length):
    password = ''.join(sample(letter, length))  # Генерируем пароль
    while password.isalpha() or password.islower():  # Если пароль не соответствует условию, вызываем функцию повторно до получения валидного пароля
        password = generate_password(length)
    return password


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]  # Создаём список из заданного количества паролей


quantity, length = map(int, input().split())
print(*generate_passwords(quantity, length), sep='\n')
