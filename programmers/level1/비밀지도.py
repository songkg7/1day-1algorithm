#
# 2018 kakao blind recruitment
# 2021/07/07 7:03 오전

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]


def solution(n, arr1, arr2):
    answer = []

    for c1, c2 in zip(arr1, arr2):
        a = bin(c1 | c2)[2:]
        a = a.zfill(n)
        a = a.replace('1', '#').replace('0', ' ')
        answer.append(a)

    return answer


print(solution(n, arr1, arr2))

# ClearTime = 2021/07/07 7:26 오전
