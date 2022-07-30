'''Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего существительно из кортежа declensions
и количества amount, в следующем формате: <количество> <существительное>
'''

from datetime import datetime


def hours(td):
    return td.seconds // 3600


def minutes(td):
    return (td.seconds // 60) % 60


def choose_plural(amount: int, declensions: tuple) -> str:
    # если amount = 0, то III склонение. Если amount = 1, то I склонение
    mnemonic = {
        0: declensions[2],
        1: declensions[0]
    }
    # если amount в диапазоне от 2 до 5 не включительно, то II склонение
    for i in range(2, 5):
        mnemonic[i] = declensions[1]
    # если amount в диапазоне от 5 до 21 не включительно, то III склонение.
    for i in range(5, 21):
        mnemonic[i] = declensions[2]
    # Находим остаток от 100, по которому и будем вычислять нужное склонение
    key = amount % 100
    return f'{amount} {mnemonic[key % 10]}' if key > 20 else f'{amount} {mnemonic[key]}'


def course(d: str):
    course_begin = datetime(2022, 11, 8, 12)
    d = datetime.strptime(d, '%d.%m.%Y %H:%M')
    if d >= course_begin:
        return 'Курс уже вышел!'
    difference = course_begin - d
    if difference.days and hours(difference):
        return f"До выхода курса осталось: {choose_plural(difference.days, ('день', 'дня', 'дней'))} и {choose_plural(hours(difference), ('час', 'часа', 'часов'))}"
    if difference.days:
        return f"До выхода курса осталось: {choose_plural(difference.days, ('день', 'дня', 'дней'))}"
    if hours(difference) and minutes(difference):
        return f"До выхода курса осталось: {choose_plural(hours(difference), ('час', 'часа', 'часов'))} и {choose_plural(minutes(difference), ('минута', 'минуты', 'минут'))}"
    if hours(difference):
        return f"До выхода курса осталось: {choose_plural(hours(difference), ('час', 'часа', 'часов'))}"
    return f"До выхода курса осталось: {choose_plural(minutes(difference), ('минута', 'минуты', 'минут'))}"


print(course(input()))
