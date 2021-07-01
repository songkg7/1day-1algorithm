#
#
# 2021/07/01 11:18 오후

import re

s = "a132"


def solution(s):
    return s.isdigit() and len(s) in (4, 6)


print(solution(s))

# ClearTime = 2021/07/01 11:41 오후
