# 1로 만들기
# DP
# 2021/06/02 1:27 오전

# TODO: 다시 풀기

N = int(input())

dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[N])
