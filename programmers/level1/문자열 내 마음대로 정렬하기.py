#
#
# 2021/07/06 1:13 오전

strings = ["abce", "abcd", "cdx"]
n = 2


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


print(solution(strings, n))

# ClearTime = 2021/07/06 1:17 오전
