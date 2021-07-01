#
#
# 2021/07/01 12:32 오후

import datetime

a, b = 5, 24


def solution(a, b):
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    idx = datetime.date(2016, a, b).weekday()
    return week[idx]


print(solution(a, b))

# ClearTime = 2021/07/01 12:54 오후
