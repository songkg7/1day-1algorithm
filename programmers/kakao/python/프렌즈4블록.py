# 2018 kakao blind recruitment
# level 2

m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ


# board1 = [['T', 'R', 'R', 'T', 'T', 'T'],
#           ['T', 'R', 'R', 'R', 'T', 'M'],
#           ['T', 'F', 'R', 'R', 'M', 'M'],
#           ['A', 'A', 'F', 'R', 'M', 'T'],
#           ['N', 'C', 'C', 'A', 'M', 'T'],
#           ['T', 'C', 'C', 'A', 'F', 'J']]


def solution(m, n, board):
    b = list(map(list, zip(*board)))
    # print(b)
    count = 0
    while True:
        pop = pop_num(b, m, n)
        if pop == 0:
            return count
        count += pop


def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                pop_set |= {(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)}
    # print(pop_set)
    for i, j in pop_set:
        # print(i, j)
        b[i][j] = 0
    # print(count)
    for i, row in enumerate(b):
        # print(i, row)
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
        # print(b[i])

    return len(pop_set)


print(solution(m, n, board))
