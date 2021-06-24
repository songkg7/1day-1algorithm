# 124 나라의 숫자
#
# 2021/06/23 11:12 오후


n = 4


def solution(n):
    answer = ''
    period = ['4', '1', '2']

    while n > 0:
        r = n % 3
        n = n // 3
        if r == 0:
            n -= 1
        answer = period[r] + answer

    return answer


print(solution(n))
