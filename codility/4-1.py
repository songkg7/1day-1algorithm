# Frog River One
# Counting Elements
# 2021/06/18 5:07 오후


def solution(X, A):
    n = set(A)
    m = set([i for i in range(1, X + 1)])

    # 절대 건너지 못하는 경우
    if n & m != m:
        return -1

    result = set()
    for i, v in enumerate(A):
        if v not in result:
            result.add(v)
            if m == result:
                return i

# ClearTime = 2021/06/18 5:21 오후 - 72%
# ClearTime = 2021/06/18 5:32 오후 - 100%
