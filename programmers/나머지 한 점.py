from collections import Counter

arr = [[1, 4], [3, 4], [3, 10]]


def solution(v):
    answer = []
    print(list(zip(*v)))

    for i in zip(*v):
        y = Counter(i)
        print(y)
        answer.extend([i for i in y if y[i] == 1])

    return answer


print(solution(arr))
