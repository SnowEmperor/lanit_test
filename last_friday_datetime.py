import calendar


def last_friday(d):
    m, y = d.split('/')
    day = calendar.monthcalendar(int(y), int(m))[-1][4]
    if not day:
        day = calendar.monthcalendar(int(y), int(m))[-2][4]
    day = str(day)
    if len(day) == 1:
        day = '0' + day
    return f'{day}.{m}.{y}'


