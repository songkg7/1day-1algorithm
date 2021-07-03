#
#
# 2021/07/03 8:14 오후

x = 2
n = 5


def solution(x, n):
    answer = [x]
    while len(answer) < n:
        answer.append(answer[-1] + x)

    return answer


print(solution(x, n))

# ClearTime = 2021/07/03 8:32 오후
