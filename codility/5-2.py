# Genomic Range Query
# Prefix Sums
# 2021/06/18 8:54 오후

from collections import Counter

A, C, G, T = 1, 2, 3, 4

S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]


def solution(S, P, Q):
    result = []
    for i in range(len(P)):

        num = 0
        arr = S[P[i]:Q[i] + 1]
        if 'A' in arr:
            num = 1
        elif 'C' in arr:
            num = 2
        elif 'G' in arr:
            num = 3
        elif 'T' in arr:
            num = 4
        result.append(num)
    return result


print(solution(S, P, Q))

# ClearTime = 2021/06/18 9:45 오후
