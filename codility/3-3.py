# Tape Equilibrium
# Arrays
# 2021/06/18 2:49 오후


A = [3, 1, 2, 4, 3]


def solution(A):
    result = []
    s = sum(A)
    t = [0] * (len(A) - 1)
    dp = [0] * (len(A) - 1)
    dp[0] = A[0]
    t[0] = s - dp[0]

    for i in range(1, len(A) - 1):
        dp[i] = dp[i - 1] + A[i]
        t[i] = s - dp[i]

    for i in range(len(dp)):
        result.append(abs(dp[i] - t[i]))

    return min(result)


print(solution(A))

# ClearTime = 2021/06/18 3:45 오후
