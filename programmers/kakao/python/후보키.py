# 2019 kakao blind recruitment
# level 2
# 이해하기 힘듬

from itertools import combinations

relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]


# 조합을 만들고 모든 조합들 중에 중복되는 조합이 있다면 그 조합방식은 제외해야한다.
# combination 과 set 을 사용해보자

# set 했을 때 길이가 줄어든다면 유일성을 통과하지 못했다고 할 수 있다.

# 비트마스크를 활용하면 쉽게 풀 수 있다.

def checkuniq(arr, row):
    return True if len(set(zip(*arr))) == row else False


def checkmin(num, unique):
    for i in unique:
        if i & num == i: return False
    return True


def solution(relation):
    relation = tuple(zip(*relation))
    col = len(relation)
    row = len(relation[0])
    candidate = []

    for num in range(1, 1 << col):
        tmp = tuple(relation[i] for i in range(col) if num & (1 << i))

        if checkuniq(tmp, row) and checkmin(num, candidate):
            candidate.append(num)

    return len(candidate)

print(solution(relation))
