# 절댓값 힙
# heap
# 2021/05/26 11:15 오후

import heapq
import sys

arr = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)

# ClearTime = 2021/05/26 11:18 오후
