#
#
# 2021/06/29 4:22 오후

n = 45


def solution(n):
    base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        base += str(mod)

    return int(base, 3)


print(solution(n))

# ClearTime = 2021/06/29 4:33 오후
