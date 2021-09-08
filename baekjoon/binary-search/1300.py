# K번째 수
# Binary Search
# 2021/06/21 11:18 오후

N = int(input())
k = int(input())


def binary_search():
    start = 1
    end = k
    result = 0
    while start <= end:
        mid = (start + end) // 2

        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)

        if count >= k:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


print(binary_search())

# ClearTime = 2021/06/22 12:07 오전
