# 토마토 (3차원)
# 그래프 탐색
# 2021/06/16 5:18 오후

from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

visited = [[[0] * M for _ in range(N)] for _ in range(H)]


def bfs():
    day = 0
    queue = deque(root)
    while queue:
        z, y, x = queue.popleft()

        visited[z][y][x] = 1

        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if visited[nz][ny][nx] == 0 and box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    queue.append([nz, ny, nx])
                    day = box[nz][ny][nx] - 1

    # 익지 않은 토마토가 있는지 검사하기
    for i in box:
        for j in i:
            if 0 in j:
                day = -1

    return day


root = []

for h in range(len(box)):
    for n in range(len(box[h])):
        for m in range(len(box[h][n])):
            if box[h][n][m] == 1:
                root.append([h, n, m])

print(bfs())

# ClearTime = 2021/06/16 5:34 오후
