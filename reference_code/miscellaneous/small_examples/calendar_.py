import calendar

cal = calendar.TextCalendar(firstweekday=0)
print(cal.formatmonth(2017, 9))
print(calendar.weekday(2017,9,23))
print(calendar.day_name[5])