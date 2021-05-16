# 월간 코드 챌린지 시즌 2
# level 2

from collections import deque

s = "("


def is_correct(string):
    input_arr = deque(string)
    string_arr = []

    while len(input_arr) > 0:
        x = input_arr.popleft()
        if not string_arr:
            string_arr.append(x)
        elif x == ')':
            if string_arr[-1] == '(':
                string_arr.pop()
        elif x == '}':
            if string_arr[-1] == '{':
                string_arr.pop()
        elif x == ']':
            if string_arr[-1] == '[':
                string_arr.pop()
        else:
            string_arr.append(x)

    if len(string_arr) > 0:
        return False
    else:
        return True


def solution(s):
    if len(s) == 1:
        return 0

    arr = deque(s)
    cnt = 0
    for _ in range(len(s)):
        if is_correct(''.join(arr)):
            cnt += 1
        arr.rotate(-1)
    return cnt


print(solution(s))
