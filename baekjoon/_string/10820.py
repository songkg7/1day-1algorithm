# TITLE: 문자열 분석
# CATEGORY: 문자열
# DATE: 2021/08/18 3:30 오후

import sys

answer = []
while True:
    strings = sys.stdin.readline().rstrip('\n')
    if not strings:
        break

    lower, upper, num, space = 0, 0, 0, 0
    for s in strings:
        for i in s:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isspace():
                space += 1
            elif i.isnumeric():
                num += 1
    print(lower, upper, num, space)

# ClearTime = 2021/08/18 3:51 오후
