#
# 2019 Kakao blind recruitment
# 2021/07/05 4:26 오전

def solution(N, stages):
    failure = [(i, 1) for i in range(1, N + 1)]
    for i in range(1, N + 1):
        if stages:
            failure[i - 1] = (i, stages.count(i) / len(stages))
            stages = list(filter(lambda x: x >= i + 1, stages))
        else:
            failure[i - 1] = (i, 0)

    return list(map(lambda x: x[0], sorted(failure, key=lambda x: -x[1])))

# ClearTime = 2021/07/05 6:11 오전
