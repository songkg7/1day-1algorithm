# 통계학
# 정렬

# 산술평균, 중앙값, 최빈값. 범위 구하기

import sys
from collections import Counter

N = int(sys.stdin.readline())

numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])


# 산술평균 : N개의 수들의 합을 N으로 나눈 값
def mean(arr):
    return round(sum(arr) / N)


# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
def median(arr):
    return arr[N // 2]


# 최빈값(mode) ; N개의 수들 중 가장 많이 나타나는 값
def mode(arr):
    mode_dict = Counter(arr)
    modes = mode_dict.most_common()
    if len(arr) > 1:
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]
    else:
        return modes[0][0]


# 범위 : N의 수들 중 최댓값과 최솟값의 차이
def scope(arr):
    return max(arr) - min(arr)


print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))
