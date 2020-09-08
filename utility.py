from datetime import datetime
from calendar import day_name


def weekDayToday():
    """ returns today's weekday name """
    return day_name[datetime.today().weekday()]


def dateToday():
    """ returns todays date in DD/MM/YYYY format """
    D = datetime.today()
    d, m, y = D.day, D.month, str(D.year)
    d = str(d) if d > 9 else '0' + str(d)
    m = str(m) if m > 9 else '0' + str(m)
    return f'{d}/{m}/{y}'


def timeNow():
    """ returns current time in HH:MM (24hr) format """
    T = datetime.now()
    h, m = T.hour, T.minute
    h = str(h) if h > 9 else '0' + str(h)
    m = str(m) if m > 9 else '0' + str(m)
    return f'{h}:{m}'
