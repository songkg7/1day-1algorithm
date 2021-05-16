# 좌표 정렬
# 정렬

N = int(input())

position = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
for pos in position:
    print(*pos)
