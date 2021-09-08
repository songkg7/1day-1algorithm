# DFS 와 BFS
# DFS, BFS
# 2021/06/11 2:03 오후

from collections import deque
from collections import defaultdict


# stack 으로 구현
def dfs(g, r):
    stack = [r]
    visited = []

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            temp = list(set(g[n]) - set(visited))
            # 작은 것부터 방문하기 위해 뒤에서부터 꺼내는 스택의 특성을 고려하여 내림차순으로 정렬 후 기존 스택에 추가.
            temp.sort(reverse=True)
            stack += temp

    return visited


# deque 로 구현
def bfs(g, r):
    queue = deque([r])
    visited = []

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            temp = list(set(g[n]) - set(visited))
            # 앞에서부터 꺼내는 로직을 고려하여 오름차순으로 정렬 후 기존 deque 에 추가.
            temp.sort()
            queue += temp

    return visited


N, M, V = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, input().split())

    # 양방향 그래프
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(*dfs(graph, V))
print(*bfs(graph, V))

# ClearTime = 2021/06/11 4:20 오후
