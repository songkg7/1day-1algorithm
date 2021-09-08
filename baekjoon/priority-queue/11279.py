# 최대 힙
# heap
# 2021/05/26 5:25 오전

import heapq
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    elif cmd > 0:
        heapq.heappush(arr, (-cmd, cmd))

# ClearTime = 2021/05/26 5:48 오전
