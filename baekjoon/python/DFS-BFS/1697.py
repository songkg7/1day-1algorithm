# 숨바꼭질
# 그래프 탐색
# 2021/06/16 5:44 오후

# 매트릭스에 수빈이가 이동할 수 있는 "최소시간"을 계속 업데이트한다.
# 그래프를 다 채우고, 해당 좌표의 값을 리턴한다.
# 목적지에 최소값이 찍힐 때?

from collections import deque

N, K = map(int, input().split())

visited = [0] * 100_001


def bfs(r, destination):
    queue = deque([r])
    visited[r] = 1
    while queue:
        if visited[destination] != 0:
            return visited[destination] - 1

        x = queue.popleft()

        dx = [1, -1, x]

        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx < 100_001:
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                else:
                    visited[nx] = min(visited[nx], visited[x] + 1)
                queue.append(nx)


print(bfs(N, K))
