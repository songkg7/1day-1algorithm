# 계단 오르기
# DP
# 2021/05/26 2:32 오전

# TODO: 다시 풀기

n = int(input())
arr = [0] * 300
for i in range(n):
    arr[i] = int(input())

dp = [0] * 300

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[2] + arr[1], arr[2] + arr[0])

for i in range(3, n):
    dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3])

print(dp[n-1])
