# 토마토
# 그래프 탐색
# 2021/06/16 12:34 오후

# 익은 토마토의 좌표를 먼저 찾아 배열에 담아놓는다.
# 전칸의 값에서 1을 증가시킨 값을 다음 토마토에 할당한다.
# 마지막에 박스를 돌면서 익지 않은 토마토가 있는지 검사한다.

from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]


def bfs():
    day = 0
    queue = deque(root)
    while queue:
        y, x = queue.popleft()

        visited[y][x] = 1

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == 0 and box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] + 1
                    queue.append([ny, nx])
                    day = box[ny][nx] - 1

                    # 박스 상태 확인 코드
                    # print('-----')
                    # print(f'{box[ny][nx] - 1}일')
                    # for i in box:
                    #     print(i)

    # 익지 않은 토마토가 있는지 검사하기
    for i in box:
        if 0 in i:
            day = -1

    return day


root = []

for n in range(len(box)):
    for m in range(len(box[n])):
        if box[n][m] == 1:
            root.append([n, m])

print(bfs())

# ClearTime = 2021/06/16 1:57 오후
