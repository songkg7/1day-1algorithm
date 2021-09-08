# 터렛
# 기본수학 2

# 삼각함수, 피타고라스 정리 활용

# 서로 다른 두 원이 겹치는 좌표(교점)의 수를 출력해야하므로
# 최대 2개가 될 수 있고 교점이 없을 수도 있다.

# 일단 두 터렛의 좌표를 바탕으로 서로 간의 거리(distance)를 구해야한다.
# 만약 두 터렛이 각자 계산한 거리 r1, r2의 합보다 거리(distance)가 더 크다면 교점은 발생하지 않는다. -> 외접일 경우
# 같다면 1개가 생기며
# 작다면 2개가 생긴다.

# 두 터렛의 위치가 동일할 수 있다. => 거리(distance)가 0일 때
# 이럴 때 r1, r2가 같다면 위치의 개수가 무한대이므로 -1 을 출력해야한다.
# r1, r2 가 다르다면 교점이 없으므로 0 이다.
import math
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    # 두 터렛 간의 거리(distance)
    c = (abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2)
    distance = math.sqrt(c)

    # 거리가 0보다 커야 같은 위치가 아니다.
    # 외접, 내접을 고려해야한다.
    r = sorted([distance, r1, r2])
    if distance > 0:
        # 외접
        if distance == r1 + r2:
            print(1)
        # 내접
        elif r[-1] == r[0] + r[1]:
            print(1)
        # 가장 긴 값이 나머지 합보다 클 경우 만나지 않는다.
        elif r[-1] > r[0] + r[1]:
            print(0)
        else:
            print(2)
    else:
        if r1 == r2:
            print(-1)
        else:
            print(0)
