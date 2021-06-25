#
# Hash
# 2021/06/26 12:15 오전

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


print(solution(participant, completion))

# ClearTime = 2021/06/26 12:35 오전
