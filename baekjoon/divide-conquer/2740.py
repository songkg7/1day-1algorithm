# 행렬 곱셈
# Divide conquer
# 2021/07/20 11:43 오전

# TODO: 다시 풀기

# -1 -2 6
# -3 -6 12
# -5 -10 18

A = []
B = []

N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for i in C:
    print(*i)

# ClearTime = 2021/07/20 12:11 오후
