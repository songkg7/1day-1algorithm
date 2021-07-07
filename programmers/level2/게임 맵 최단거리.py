#
#
# 2021/07/07 10:34 오후

from collections import deque

maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1]]


def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # BFS
    while queue:
        x, y = queue.popleft()

        # 목적지 도달, 게임 종료 조건
        if x == m - 1 and y == n - 1:
            answer = visited[y][x]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # maps 의 범위를 벗어나지 않고, 방문한 적이 없으며, 벽이 아닌 좌표일 때
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and maps[ny][nx] != 0:
                # 도달거리
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))

    return answer


print(solution(maps))

# ClearTime = 2021/07/07 11:05 오후
