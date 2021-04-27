# 2019 kakao blind recruitment
# level 2

from itertools import combinations
from collections import Counter

relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]


# 조합을 만들고 모든 조합들 중에 중복되는 조합이 있다면 그 조합방식은 제외해야한다.
# combination 과 set 을 사용해보자

# 하나의 원소를 선택해서 같은 원소가 다른 모든 배열 안에 들어있는지 검색해본다.
# 들어있지 않다면 후보키가 될 수 있다.

# 두 원소를 선택해서 위의 과정을 반복해본다.

def solution(relation):

    for student in relation:
        for i in range(1, len(student)):
            cond = combinations(student, i)
            for info in cond:
                print(info)

    # cond = list(zip(*relation))
    # for column in cond:
    #     # print(column)
    #     if len(set(column)) == len(column):
    #         print(column)

print(solution(relation))
