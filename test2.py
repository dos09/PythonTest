from datetime import datetime
from datetime import timedelta

year = int(input())

if year != 1918:
    if year < 1918:
        is_leap = year % 4 == 0
    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and not(year % 100 == 0)) 
    pday = datetime.strptime('{0}-{1}-{2}'.format(year, 9, 12 if is_leap else 13),
                             '%Y-%m-%d')
else:
    pday = datetime.strptime('1918-02-14', '%Y-%m-%d') + timedelta(days=256-32)
print(pday.strftime('%d.%m.%Y'))