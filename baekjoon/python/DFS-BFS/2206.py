# 벽 부수고 이동하기
# 그래프 탐색
# 2021/06/17 9:16 오전

# 3차원 배열 활용

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]


def bfs():
    visited[0][0][0] = 1
    queue = deque([[0, 0, 0]])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        w, x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return max(visited[0][x][y], visited[1][x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[w][nx][ny] == 0 and graph[nx][ny] != 1:
                    visited[w][nx][ny] = visited[w][x][y] + 1
                    queue.append([w, nx, ny])

                # 벽을 뚫은 적이 없는 상태에서 벽을 만난다면 겹쳐져 있는 3차원 배열의 다른 쪽으로 넘어가자.
                elif visited[1][nx][ny] == 0 and graph[nx][ny] == 1 and w == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    queue.append([1, nx, ny])
    return -1


print(bfs())

# ClearTime = 2021/06/17 10:44 오전
