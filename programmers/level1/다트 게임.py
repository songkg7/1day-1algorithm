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
        'T': 3
    }

    count = []

    while dart_result:
        result = p.search(dart_result)
        # print(p.findall(dart_result))

        point = int(result.group("point"))
        bonus = result.group("bonus")
        option = result.group("option")

        count.append(point ** point_data[bonus])
        if option == '*':
            count[-1] *= 2
            if len(count) > 1:
                count[-2] *= 2
        elif option == '#':
            count[-1] *= -1

        dart_result = dart_result[result.end():]

    return sum(count)


print(solution(dart_result))

# ClearTime = 2021/07/09 11:47 오전
