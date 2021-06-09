# 포도주 시식
# DP
# 2021/06/09 7:26 오후

n = int(input())

dp = [0] * (n + 1)
w = [0]
for _ in range(n):
    w.append(int(input()))

dp[1] = w[1]
dp[2] = w[1] + w[2]
if n > 2:
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i])

print(dp[n])

# ClearTime = 2021/06/09 7:59 오후
