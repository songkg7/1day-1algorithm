# 월간 코드 챌린지 시즌 2
# level 1

l = 24
r = 27


def solution(left, right):
    num = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1

        if cnt % 2 == 0:
            num += i
        else:
            num -= i
    return num


print(solution(l, r))
