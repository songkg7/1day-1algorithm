# 연습문제
# level 2

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]


def solution(arr1, arr2):
    # N * M, M * K 행렬의 곱
    N = len(arr1)
    M = len(arr1[0])
    K = len(arr2[0])

    C = [[0 for _ in range(K)] for _ in range(N)]

    print(C)

    for n in range(N):
        for k in range(K):
            for m in range(M):
                C[n][k] += arr1[n][m] * arr2[m][k]

    return C


print(solution(arr1, arr2))
