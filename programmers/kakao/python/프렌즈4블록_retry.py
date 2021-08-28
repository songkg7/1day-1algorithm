m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]


# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ

def solution(m, n, board):
    b = list(map(list, zip(*board)))

    count = 0
    while True:
        pop = pop_num(b,m,n)
        if pop ==0:
            return count
        count += pop


def pop_num(b, m, n):
    pop_set = set()
    for i in range(1, n):
        for j in range(1, m):
            # print(b[i][j])
            if b[i][j] == b[i][j - 1] == b[i - 1][j] == b[i - 1][j - 1] != '_':
                pop_set |= {(i, j), (i, j - 1), (i - 1, j), (i - 1, j - 1)}

    for i, j in pop_set:
        b[i][j] = 0

    for i, row in enumerate(b):
        empty = ['_'] * row.hit(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)


print(solution(m, n, board))
