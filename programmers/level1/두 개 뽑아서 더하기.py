# 두 개 뽑아서 더하기
# level 1

numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            answer.append(numbers[i] + j)
    return sorted(list(set(answer)))


print(solution(numbers))
