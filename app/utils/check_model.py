import datetime
from app.exception.model_exception import YearOutOfRangeException, DayOutOfRangeException, MonthOutOfRangeException


# Funcion encargada de comprobar que el año ingresado es valido
def check_year(year):
    current_time = datetime.datetime.now()
    date = current_time.date()
    actual_year = date.strftime("%Y")

    if int(year) > int(actual_year) or int(year) <= 2012:
        raise YearOutOfRangeException()


# Funcion encargada de comprobar que el mes ingresado es valido
def check_month(month):
    month_abbreviated = {
        '1': 'Ene',
        '2': 'Feb',
        '3': 'Mar',
        '4': 'Abr',
        '5': 'May',
        '6': 'Jun',
        '7': 'Jul',
        '8': 'Ago',
        '9': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dic'
    }

    short_month = month_abbreviated.get(month.lower())
    if short_month is None:
        raise MonthOutOfRangeException()
    return short_month


# Funcion ecargada de comprobar que el dia ingresado es valido
def check_day(day):
    if int(day) < 1 or int(day) > 31:
        raise DayOutOfRangeException()
    return day
