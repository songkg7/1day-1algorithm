# 색종이 만들기
# Divide and Conquer
# 2021/06/22 8:29 오후

# TODO: 다시 풀기

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = []


def quad_tree(x, y, n):
    color = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != matrix[i][j]:
                quad_tree(x, y, n // 2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


quad_tree(0, 0, N)
print(result.count(0))
print(result.count(1))
