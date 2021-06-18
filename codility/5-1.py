# Count Div
# Prefix Sums
# 2021/06/18 8:16 오후

A, B, K = 6, 11, 2


def solution(A, B, K):
    na = A // K
    ra = A % K
    nb = B // K
    count = nb - na
    if ra == 0:
        count += 1
    return count


print(solution(A, B, K))

# ClearTime = 2021/06/18 8:53 오후
