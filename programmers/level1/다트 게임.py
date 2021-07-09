#
# 2018 kakao blind recruitment
# 2021/07/09 11:00 오전

import re

dart_result = "1S2D*3T"


def solution(dart_result):
    p = re.compile(r"(?P<point>\d+)(?P<bonus>[SDT])(?P<option>[*#]?)")

    point_data = {
        'S': 1,
        'D': 2,
        'T': 3,
        '': 1,
        '*': 2,
        '#': -1
    }

    darts = p.findall(dart_result)
    print(darts)
    for i in range(len(darts)):
        if darts[i][2] == '*' and i > 0:
            darts[i - 1] *= 2
        darts[i] = int(darts[i][0]) ** point_data[darts[i][1]] * point_data[darts[i][2]]

    return sum(darts)


print(solution(dart_result))

# ClearTime = 2021/07/09 11:47 오전
