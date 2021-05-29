# 회전하는 큐
# queue
# 2021/05/25 12:29 오후

# 회전 방향을 선택하는 문제
# TODO: 정리하기

from collections import deque

N, M = map(int, input().split())

que = deque([i for i in range(1, N + 1)])
wanted = list(map(int, input().split()))

# wanted 의 숫자가 que 어디에 있는지 index 를 찾아서 전체 길이에서 위치를 비교해보자
rotation_count = 0
for num in wanted:

    while num != que[0]:
        if que.index(num) <= (len(que) / 2):
            rotation_count += 1
            que.rotate(-1)
        else:
            rotation_count += 1
            que.rotate(1)

    que.popleft()

print(rotation_count)

# ClearTime = 1:01 오후
