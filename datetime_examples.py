import datetime
from datetime import date, datetime, timedelta

print(date.today())
print(date.today().strftime(
    'today - %d.%m.%Y'
))

print(datetime.today())
print(datetime.today().strftime(
    '%d.%m.%Y %H:%M:%S'
))

a = datetime(2022, 9, 27, 12, 34)
print(a.date())
print(a.time())
print(a.strftime('%d.%m.%Y %H:%M:%S'))

b = datetime.strptime(
    '27.09.2022 10:34:00',
    '%d.%m.%Y %H:%M:%S'
)
print('date from strptime', b)


c = a + timedelta(hours=1, minutes=30)
print(c)
