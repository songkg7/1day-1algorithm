# 수 찾기
# Binary Search
# 2021/06/15 5:22 오전

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()


def binary_search(v, li):
    start = 0
    end = len(li) - 1

    while start <= end:
        mid = (start + end) // 2
        if li[mid] == v:
            return True
        elif li[mid] < v:
            start = mid + 1
        else:
            end = mid - 1

    return False


for num in nums:
    print(1 if binary_search(num, A) else 0)

# ClearTime = 2021/06/15 6:00 오전
