# 괄호

# 길이가 홀수이면 무조건 NO를 출력

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    stack = []
    string = sys.stdin.readline().strip()

    p = 0
    for s in string:
        if s == '(':
            p += 1
        else:
            p -= 1

        if p < 0:
            print('NO')
            break
    if p > 0:
        print('NO')
    elif p == 0:
        print('YES')
