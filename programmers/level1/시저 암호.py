#
#
# 2021/07/19 2:27 오전

# FIXME: 효율성이 좋지 못함.

s = "a B z"
n = 4


def solution(s, n):
    string = list(map(ord, s))

    while n > 0:
        for i in range(len(string)):
            if 65 <= string[i] < 90 or 97 <= string[i] < 122:
                string[i] += 1
            elif string[i] == 90:
                string[i] = 65
            elif string[i] == 122:
                string[i] = 97
        n -= 1

    answer = list(map(chr, string))
    return ''.join(answer)


print(solution(s, n))

# ClearTime = 2021/07/19 2:44 오전
