# 가장 긴 증가하는 부분 수열
# DP
# 2021/05/27 12:21 오후

# TODO: 다시 풀기

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
