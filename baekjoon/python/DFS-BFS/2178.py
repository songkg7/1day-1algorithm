# 미로 탐색
# 그래프 탐색
# 2021/06/12 11:17 오전

# TODO: 다시 풀기

from collections import deque

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

# count 를 증가시키면서 탐색, 목표에 도착하는 순간 break
# 목표 인덱스 [N-1][M-1]
# 목표에 도달하는 순간은? visited[N-1][M-1] 가 꺼내질 때

root = 0


def bfs(g):
    visited = [[0] * M for _ in range(N)]
    queue = deque([[0, 0]])
    visited[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            print(visited[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and g[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.extend([[nx, ny]])


bfs(maze)

# ClearTime = 2021/06/12 12:02 오후
