#
# 월간 코드 챌린지 시즌 1
# 2021/07/21 10:27 오후

s = "110010101001"


def solution(s):
    count = 0  # 함수 실행 카운트
    result = 0  # 제거된 0의 개수
    while s != "1":
        count += 1

        length = len(s)  # 최초 길이

        remove_zero = s.replace("0", '')
        a = len(remove_zero)  # 0 제거 후 길이

        # 제거한 0의 개수
        result += length - a

        # 이진 변환 결과
        s = bin(a)[2:]

    return [count, result]


print(solution(s))

# ClearTime = 2021/07/21 10:50 오후
