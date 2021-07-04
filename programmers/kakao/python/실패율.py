#
# 2019 Kakao blind recruitment
# 2021/07/05 4:26 오전

from collections import Counter

N = 6
stages = [4,4,4,4,4]


def solution(N, stages):
    dp = stages
    failure = [(1, dp.count(1) / len(dp))] + [(i, 1) for i in range(2, N+1)]
    for i in range(2, N + 1):
        if dp:
            failure[i-1] = (i, dp.count(i) / len(dp))
            dp = list(filter(lambda x: x >= i + 1, dp))

    return list(map(lambda x: x[0], sorted(failure, key=lambda x: -x[1])))


print(solution(N, stages))
