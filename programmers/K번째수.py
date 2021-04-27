# 정렬
# level 1

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        sorted_array = sorted(array[i - 1:j])
        answer.append(sorted_array[command[2] - 1])

    return answer


print(solution(array, commands))
