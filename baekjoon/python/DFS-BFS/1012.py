# 유기농 배추
# 그래프 탐색
# 2021/06/12 10:44 오전


def dfs(x, y):
    visited[y][x] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                dfs(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    visited = [[0] * M for _ in range(N)]
    matrix = [[0] * M for _ in range(N)]
    for _ in range(K):
        n1, n2 = map(int, input().split())
        matrix[n2][n1] = 1

    count = 0
    for a in range(M):
        for b in range(N):
            if matrix[b][a] == 1 and visited[b][a] == 0:
                count += 1
                dfs(a, b)

    print(count)

# ClearTime = 2021/06/12 11:12 오전
