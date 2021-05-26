# 최소 힙
# heap
# 2021/05/26 6:27 오후

import heapq
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, x)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)

# ClearTime = 2021/05/26 6:31 오후
