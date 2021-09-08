# 네 번째 점
# 기본수학 2

# 직사각형을 만들기 위해서는 같은 x 좌표가 2개, 같은 y 좌표가 2개 있어야한다.

x = []
y = []

for _ in range(3):
    p1, p2 = map(int, input().split())
    x.append(p1)
    y.append(p2)

    if x.count(p1) == 2:
        x.remove(p1)
        x.remove(p1)

    if y.count(p2) == 2:
        y.remove(p2)
        y.remove(p2)

print(f'{x[0]} {y[0]}')

