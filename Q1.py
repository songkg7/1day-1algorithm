# 두 개 뽑아서 더하기

numbers = [2, 1, 3, 4, 1]

def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            answer.append(numbers[i] + j)
    return sorted(list(set(answer)))

# def solution(numbers):
#     answer = []

#     for i in range(0, len(numbers) - 1):
#         for j in numbers[i + 1:]:
#             s = numbers[i] + j
#             if not s in answer:
#                 answer.append(s)
#     answer.sort()
#     return answer

print(solution(numbers))