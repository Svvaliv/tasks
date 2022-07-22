import calendar
from datetime import date, timedelta

months = {month: index for index, month in enumerate(calendar.month_name) if month}


def get_all_mondays(year: int) -> list[date]:
    mondays = []
    today = date(year, 1, 1)
    while calendar.day_name[today.weekday()] != 'Monday':
        today += timedelta(days=1)
    while today.year < year + 1:
        mondays.append(today)
        today += timedelta(days=7)
    return mondays


