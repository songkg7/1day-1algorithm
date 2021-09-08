# 랜선 자르기
# Binary Search
# 2021/06/19 1:54 오후

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]


def binary_search():
    start = 1
    end = max(lines)
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for lan in lines:
            count += lan // mid

        if count >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(binary_search())

# ClearTime = 2021/06/19 2:07 오후
