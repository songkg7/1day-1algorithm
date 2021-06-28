#
# 완전탐색
# 2021/06/29 1:19 오전

answers = [1, 3, 2, 4, 2]


def solution(answers):
    def exam(student):
        count = 0
        for i, j in zip(student, answers):
            if i == j:
                count += 1
        return count

    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    result = [(exam(s1), 1), (exam(s2), 2), (exam(s3), 3)]
    return list(map(lambda x: x[1], filter(lambda x: x[0] == max(result)[0], result)))


print(solution(answers))
