# Функция получает на вход текст вида:
# “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime, timedelta
from module.task3 import logging_decorator

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
    month = months[month]
    weekday = weekdays[weekday]
    date_ = datetime(year=datetime.now().year, month=month, day=1)
    result = date_ + timedelta(weeks=weeks - 1, days=(weekday - date_.weekday() + 7) % 7)
    if result.month != month:
        raise ValueError('Такой даты не существует!')
    return result
