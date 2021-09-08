# TITLE: !밀비 급일
# CATEGORY: 문자열
# DATE: 2021/08/19 2:20 오후

import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == 'END':
        break

    print(s[::-1])

# ClearTime = 2021/08/19 2:23 오후
