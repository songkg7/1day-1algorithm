# 달팽이는 올라가고 싶다

# 낮에 A 미터 올라가고 밤에 B 미터만큼 미끄러진다.
# 나무의 높이는 V 미터일때 꼭대기까지 올라가려면 며칠이 걸리는가?

# A, B, V = 100, 99, 1000000000

# position = 0
# dayCount = 0

# while position < V:
#     dayCount += 1
#     position += A
#     if position >= V:
#         break
#     position -= B
#
# print(dayCount)

# 위 방법은 정답은 나오지만 시간제한을 통과하지 못한다.

# 다음과 같은 방법을 생각해볼 수 있다.

# V - A => 마지막날 전까지 이동한 거리 = X
# A - B => 하루동안 이동할 수 있는 거리 = Y
# (V - A) 를 (A - B) 로 나누고(마지막날 전까지 이동한 날짜수) + 1(마지막날)을 하게 되면 정답이 나오지 않을까

import math

A, B, V = map(int, input().split(" "))

X = V - A
Y = A - B

dayCount = math.ceil(X / Y + 1)

print(dayCount)
