# 포비와 크롱
# 우아한 테크코스
# 2021/06/03 11:10 오후

# 1 ~ 400 page

# pobi 와 crong 의 길이는 2

pobi = [131, 132]  # 곱해서 72 가 가장 큰 수
crong = [211, 212]  # 곱해서 72가 가장 큰 수 => 무승부


def sum_page(arr):
    result = []
    for i in arr:
        i = str(i)
        result.append(sum(map(int, i)))
    return max(result)


def multiply_page(arr):
    result = []
    for i in arr:
        count = 1
        i = list(map(int, str(i)))
        for j in i:
            count *= j
        result.append(count)
    return max(result)


def solution(arr1, arr2):
    if arr1[1] - arr1[0] != 1 or arr2[1] - arr2[0] != 1:
        return -1

    p_score = max(sum_page(arr1), multiply_page(arr1))
    c_score = max(sum_page(arr2), multiply_page(arr2))

    if p_score > c_score:
        answer = 1
    elif p_score < c_score:
        answer = 2
    else:
        answer = 0
    return answer


print(solution(pobi, crong))

# ClearTime = 2021/06/03 11:32 오후
