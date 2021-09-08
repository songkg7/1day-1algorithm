# 큐 2
# queue

# 연산당 시간복잡도 O(1) 을 만족시켜라

from collections import deque
import sys

N = int(sys.stdin.readline())

queue = deque()
for _ in range(N):
    commands = sys.stdin.readline().split()
    cmd = commands[0]
    if cmd == "push":
        queue.append(commands[1])
    elif cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
