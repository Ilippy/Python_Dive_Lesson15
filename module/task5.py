# Дорабатываем задачу 4. Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

from datetime import timedelta, datetime
from module.task3 import logging_decorator
import argparse

months = {'января': 1, 'февраля': 2, 'марта': 3,
          'апреля': 4, 'мая': 5, 'июня': 6,
          'июля': 7, 'августа': 8, 'сентября': 9,
          'октября': 10, 'ноября': 11, 'декабря': 12}

weekdays = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,
            'пятница': 4, 'суббота': 5, 'воскресенье': 6}


@logging_decorator
def date_from_text(date: str) -> datetime:
    day, weekday, month = date.split()
    weeks = int(day[0])
    month = int(month) if month.isdigit() else months[month]
    weekday = weekdays[weekday]
    date_ = datetime(year=datetime.now().year, month=month, day=1)
    result = date_ + timedelta(weeks=weeks - 1, days=(weekday - date_.weekday() + 7) % 7)
    if result.month != month:
        raise ValueError('Такой даты не существует!')
    return result


def out_parser():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-w', '--week', metavar='week', default='1')
    parser.add_argument('-d', '--weekday', metavar='weekday', default='понедельник')
    parser.add_argument('-m', '--month', metavar='month', default='1')
    result = parser.parse_args()
    return " ".join((result.week, result.weekday, result.month))
