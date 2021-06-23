# 이분 그래프
# 그래프 탐색
# 2021/06/17 12:37 오후

# TODO: 다시 풀기

from collections import deque
import sys

input = sys.stdin.readline
k = int(input())


def bfs(start):
    visited[start] = 1
    queue = deque([start])
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = -visited[n]
                queue.append(i)
            else:
                if visited[i] == visited[n]:
                    return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    isTrue = True
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(graph)

    for k in range(1, v + 1):
        if visited[k] == 0 and not bfs(k):
            isTrue = False
            break
    print("YES" if isTrue else "NO")
