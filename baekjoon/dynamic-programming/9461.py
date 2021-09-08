# 파도반 수열
# DP
# 2021/05/25 11:22 오후

T = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for _ in range(T):
    N = int(input())
    if N < 4:
        print(dp[N])
    else:
        for k in range(4, N + 1):
            dp[k] = dp[k - 3] + dp[k - 2]
        print(dp[N])

# ClearTime = 11:28 오후
