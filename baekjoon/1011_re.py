# Fly me to the Alpha Centauri
# 기본수학 1

# Point.
# 이동해야할 목적지까지 거리의 절반까지만 도달하면 지금까지 온 이동횟수만큼만 더 가면된다.
import math

x, y = 45, 50

d = y - x  # 이동해야하는 거리

v = 0  # 현재 속도
m = 0  # 현재까지 이동한 거리
n = 0  # 공간이동 횟수

# print(d%2)
if d % 2 != 0:
    d -= 1

for v in range(1, d + 1):
    if m >= d / 2:
        break
    # print(v)

    m += v
    n += 1

print(m)
print(n)
if (y - x) % 2 != 0:
    print(f'answer = {n * 2 + 1}')
else:
    print(f'answer = {n * 2}')
