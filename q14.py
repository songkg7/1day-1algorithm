import collections

# 완주하지 못한 선수
# 프로그래머스
# level 1

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):

    a = sorted(participant)
    b = sorted(completion)

    for i in range(len(a)):
        if (i == len(a)-1):
            return a[i]

        if (a[i] != b[i]):
            return a[i]

print(solution(participant, completion))

def solution2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]