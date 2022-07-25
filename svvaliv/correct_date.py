from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except (ValueError, TypeError):
        return False


# Вводим дату в формате "DD.MM.YYYY"
date_ = input()
correct_dates = 0

# Проверяем дату и вводим следующую, для выхода вводим "end"
while date_ != 'end':
    day, month, year = map(int, date_.split('.'))
    if is_correct(day, month, year):
        correct_dates += 1
        print('Корректная')
    else:
        print('Некорректная')
    date_ = input()
print(correct_dates)
