#
#
# 2021/07/01 11:18 오후

import re

s = "12a4"


def solution(s):
    if len(s) == 4 or len(s) == 6:
        p = re.compile(r"\d")
        m = p.findall(s)
        if len(m) == len(s):
            return True
        else:
            return False
    else:
        return False


print(solution(s))

# ClearTime = 2021/07/01 11:41 오후
