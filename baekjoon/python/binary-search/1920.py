# 수 찾기
# Binary Search
# 2021/06/15 5:22 오전

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# 시간초과일 경우 다른 정렬방법 사용하기
A.sort()


def binary_search(v, li):
    if len(li) == 1 and v != li[0]:
        return False

    mid = len(li) // 2

    if v == li[mid]:
        return True

    if v < li[mid]:
        li = li[:mid]
        return binary_search(v, li)
    else:
        li = li[mid:]
        return binary_search(v, li)


for num in nums:
    if binary_search(num, A):
        print(1)
    else:
        print(0)

# ClearTime = 2021/06/15 6:00 오전
