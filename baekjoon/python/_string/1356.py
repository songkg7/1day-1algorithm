# TITLE: 유진수
# CATEGORY: 문자열
# DATE: 2021/08/27 8:00 오후

from functools import reduce

N = input()

answer = "NO"
for i in range(1, len(N)):
    prev = reduce(lambda x, y: x * y, map(int, list(N[:i])))
    cur = reduce(lambda x, y: x * y, map(int, list(N[i:])))
    if prev == cur:
        answer = "YES"
        break

print(answer)

# ClearTime = 2021/08/27 8:12 오후
