# 숨바꼭질
# 그래프 탐색
# 2021/06/16 5:44 오후

# 매트릭스에 수빈이가 이동할 수 있는 "최소시간"을 계속 업데이트한다.
# 그래프를 다 채우고, 해당 좌표의 값을 리턴한다.
# 목적지에 최소값이 찍힐 때?

from collections import deque

N, K = map(int, input().split())
visited = [0] * 100_001


def bfs():
    queue = deque([N])

    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100_001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)


print(bfs())

# ClearTime = 2021/06/16 7:15 오후
