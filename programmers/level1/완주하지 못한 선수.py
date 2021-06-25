#
# Hash
# 2021/06/26 12:15 오전

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    data = dict()
    for p in participant:
        if p not in data:
            data[p] = 1
        else:
            data[p] += 1

    for c in completion:
        data[c] += 1

    a = list(filter(lambda x: x[1] % 2 == 1, data.items()))
    return a[0][0]


print(solution(participant, completion))

# ClearTime = 2021/06/26 12:35 오전
