# 요세푸스 문제 0
# queue
# 2021/05/25

from collections import deque

N, K = map(int, input().split())

josephus = deque([i for i in range(1, N + 1)])

perm = []
while josephus:
    josephus.rotate(-K + 1)
    perm.append(josephus.popleft())

print('<' + str(perm)[1:-1] + '>')
