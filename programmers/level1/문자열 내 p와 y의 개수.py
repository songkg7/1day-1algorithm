#
#
# 2021/07/04 12:52 오후

from collections import Counter

s = "af"


def solution(s):
    t = Counter(s.lower())
    return t["p"] == t["y"]


print(solution(s))

# ClearTime = 2021/07/04 12:59 오후
