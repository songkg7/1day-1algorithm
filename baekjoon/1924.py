# TITLE: 2007년
# CATEGORY:
# DATE: 2021/11/04 9:23 오후

import datetime

weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

month, day = map(int, input().split())

date = datetime.date(2007, month, day).weekday()

print(weekdays[date])

# ClearTime = 2021/11/04 9:29 오후
