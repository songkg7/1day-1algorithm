# 바이러스
# DFS 와 BFS
# 2021/06/11 11:00 오후

# len(visited) - 1 을 출력

from collections import deque


def bfs_network_count(g, r):
    queue = deque([r])
    visited = []

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += list(set(g[n]) - set(visited))

    return len(visited) - 1


N = int(input())
edge_count = int(input())

graph = {}
for _ in range(edge_count):
    n1, n2 = map(int, input().split())

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(bfs_network_count(graph, 1))

# ClearTime = 2021/06/11 11:18 오후
