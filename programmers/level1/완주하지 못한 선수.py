#
# Hash
# 2021/06/26 12:15 오전

from collections import Counter

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = list(Counter(participant) - Counter(completion))
    return answer[0]


print(solution(participant, completion))

# ClearTime = 2021/06/26 12:35 오전
