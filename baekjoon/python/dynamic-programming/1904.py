# 01타일
# DP
# 2021/05/25 10:56 오후

# "00", "1"

# TODO: 다시 풀기

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3, n + 1):
    dp[k] = (dp[k - 1] + dp[k - 2]) % 15746
print(dp[n])
