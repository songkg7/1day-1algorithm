#
# 월간 코드 챌린지 시즌 1
# 2021/07/21 10:27 오후

s = "110010101001"


def solution(s):
    count = 0  # 함수 실행 카운트
    result = 0  # 제거된 0의 개수
    while s != "1":
        count += 1
        num = s.count('1')
        result += len(s) - num
        s = bin(num)[2:]

    return [count, result]


print(solution(s))

# ClearTime = 2021/07/21 10:50 오후
