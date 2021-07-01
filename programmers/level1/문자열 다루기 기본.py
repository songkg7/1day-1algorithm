#
#
# 2021/07/01 11:18 오후

import re

s = "1234"


def solution(s):
    return bool(re.match(r"^(\d{4}|\d{6})$", s))


print(solution(s))

# ClearTime = 2021/07/01 11:41 오후
