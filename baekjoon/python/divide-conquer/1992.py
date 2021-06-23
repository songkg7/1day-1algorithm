# 쿼드트리
# Divide and Conquer
# 2021/06/22 8:57 오후

# TODO: 정리하기

N = int(input())
matrix = [list(input()) for _ in range(N)]

result = []


def quad_tree(y, x, n):
    color = matrix[x][y]

    if n == 1:
        result.append(matrix[x][y])
        return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != matrix[i][j]:  # matrix 안에 다른 색의 점이 있다.
                # 반 접기
                result.append('(')
                quad_tree(y, x, n // 2)
                quad_tree(y + n // 2, x, n // 2)
                quad_tree(y, x + n // 2, n // 2)
                quad_tree(y + n // 2, x + n // 2, n // 2)
                result.append(')')
                return

    if color == '0':
        result.append('0')
    else:
        result.append('1')


quad_tree(0, 0, N)
print(''.join(result))

# ClearTime = 2021/06/22 9:37 오후
