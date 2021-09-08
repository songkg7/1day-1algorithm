# 나이트의 이동
# 그래프 탐색
# 2021/06/17 11:53 오전

from collections import deque

# 나이트의 이동 위치
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(root, d, length):
    # 체스판 설정
    board = [[0] * length for _ in range(length)]

    # 방문할 위치
    queue = deque([root])

    while queue:
        x, y = queue.popleft()
        if x == d[0] and y == d[1]:
            return board[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append([nx, ny])


T = int(input())
for _ in range(T):
    L = int(input())
    cur = map(int, input().split())
    destination = list(map(int, input().split()))
    print(bfs(cur, destination, L))

# ClearTime = 2021/06/17 12:14 오후
