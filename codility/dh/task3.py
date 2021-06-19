#
#
# 2021/06/19 7:39 오후

# 1990 1 31 이후

import datetime
import re

S = open("../delivery-hero/test.txt")


def solution(S):
    count = 0
    p = re.compile(r"(?P<size>\d+)\s(?P<day>\d+)\s(?P<month>\w+)\s(?P<year>\d+)\s(?P<file>[\w!-.]+)")

    lists = list(map(lambda x: x.strip(), S.readlines()))

    for i in lists:
        size = int(p.match(i).group("size"))
        day = int(p.match(i).group("day"))
        month = 1 if p.match(i).group("month") == "Jan" else 2
        year = int(p.match(i).group("year"))

        date = datetime.date(year, month, day)
        limit = datetime.date(1990, 1, 31)

        if size >= 240 * (2 ** 10) and date > limit:
            count += 1
    return count


print(solution(S))

# ClearTime = 2021/06/19 9:13 오후
