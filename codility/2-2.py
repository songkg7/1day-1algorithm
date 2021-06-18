# Odd Occurrences In Array
# Arrays
# 2021/06/17 6:45 오후

# 문제의 설명에서 A의 값 중 하나를 제외한 모든 값이 짝수로 발생한다 하였다.

from collections import Counter


def solution(A):
    n = Counter(A)
    return list(filter(lambda x: x[1] % 2 != 0, n.items()))[0][0]

# ClearTime = 2021/06/17 6:54 오후
