#
#
# 2021/06/19 6:58 오후

import numpy

S = "aaaaaaaaa"


def solution(S):
    count = 0
    if S.hit('a') < 3:
        return 0

    s = list(S)

    for i in range(2, len(s)):
        for j in range(1, i):
            arr = numpy.split(s, [j, i])
            num = set()
            for k in range(len(arr)):
                num.add(list(arr[k]).count('a'))
            print(num)
            if len(num) == 1:
                count += 1

    return count


print(solution(S))

# ClearTime = 2021/06/19 7:33 오후
