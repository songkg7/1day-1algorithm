# TITLE: 연결 요소의 개수
# CATEGORY: 그래프 이론
# DATE: 2021/09/04 10:23 오후

import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
nodes = defaultdict(list)
for _ in range(M):
    n, v = map(int, sys.stdin.readline().split())
    nodes[n] = nodes.get(n, []) + [v]
    nodes[v] = nodes.get(v, []) + [n]

visited = []


def bfs(root):
    stack = [root]
    while stack:
        next_node = stack.pop()
        for i in nodes[next_node]:
            if i not in visited:
                stack.append(i)
                visited.append(i)


answer = 0
for i in range(1, N + 1):
    if i not in visited:
        bfs(i)
        answer += 1

print(answer)

# ClearTime = 2021/09/04 11:08 오후
