# TITLE: 큐
# CATEGORY: 자료구조
# DATE: 2021/08/24 7:30 오후

import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(0 if queue else 1)
    elif cmd[0] == 'front':
        print(queue[0] if queue else -1)
    elif cmd[0] == 'back':
        print(queue[-1] if queue else -1)

# ClearTime = 2021/08/24 11:04 오후 - sys 사용하지 않으면 시간초과
