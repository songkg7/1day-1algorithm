# 종이의 개수
# Divide and Conquer
# 2021/06/22 10:36 오후

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = {
    -1: 0,
    0: 0,
    1: 0
}


def divide(x, y, n):
    paper = matrix[x][y]
    if n == 1:
        result[paper] += 1
        return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper != matrix[i][j]:
                gap = n // 3

                divide(x, y, gap)
                divide(x + gap, y, gap)
                divide(x + gap * 2, y, gap)
                divide(x + gap * 2, y + gap, gap)
                divide(x, y + gap, gap)
                divide(x, y + gap * 2, gap)
                divide(x + gap, y + gap * 2, gap)
                divide(x + gap, y + gap, gap)
                divide(x + gap * 2, y + gap * 2, gap)
                return

    result[paper] += 1


divide(0, 0, N)
for i in result.values():
    print(i)

# ClearTime = 2021/06/22 11:00 오후
