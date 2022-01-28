# TITLE: 없는 숫자 더하기
# CATEGORY: level 1
# DATE: 2022/01/28 8:24 PM

numbers = [1, 2, 3, 4, 6, 7, 8, 0]


def solution(numbers):
    origin = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    for candidate in origin:
        if candidate not in numbers:
            answer += candidate

    return answer


print(solution(numbers))

# ClearTime = 2022/01/28 8:32 PM
