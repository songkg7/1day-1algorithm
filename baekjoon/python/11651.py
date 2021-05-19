# 좌표 정렬하기 2
# 정렬

N = int(input())

position = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
for i in position:
    print(*i)
