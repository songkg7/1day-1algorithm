# 가운데를 말해요
# priority queue
# 2021/07/18 9:07 오후

# TODO: 다시 풀기

import heapq
import sys

left, right = [], []
N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        # max heap
        heapq.heappush(left, (-num, num))
    else:
        # min heap
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))

    print(left[0][1])

# ClearTime = 2021/07/18 9:16 오후 - time over
