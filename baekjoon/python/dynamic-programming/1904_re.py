# 01 타일
# DP
# 2021/06/05 8:19 오후

# 0, 1 | 1, 2, 3, 5, 8, ...

import sys

N = int(sys.stdin.readline())


def fibonacci(n):
    val = [0, 1]
    if n < 2:
        return val[n]
    else:
        for i in range(2, n + 1):
            val.append((val[i - 1] + val[i - 2]) % 15746)
        return val[n]


print(fibonacci(N + 1))

# ClearTime = 2021/06/05 9:05 오후
