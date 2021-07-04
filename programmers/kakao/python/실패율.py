#
# 2019 Kakao blind recruitment
# 2021/07/05 4:26 오전

def solution(N, stages):
    failure = {}

    for i in range(1, N + 1):
        if stages:
            failure[i] = stages.count(i) / len(stages)
            stages = list(filter(lambda x: x >= i + 1, stages))
        else:
            failure[i] = 0

    return sorted(failure, key=lambda x: failure[x], reverse=True)

# ClearTime = 2021/07/05 6:11 오전
