# 나무 자르기
# Binary Search
# 2021/06/19 2:15 오후

N, M = map(int, input().split())
trees = list(map(int, input().split()))


def binary_search():
    start = 1
    end = max(trees)

    while start <= end:
        wood = 0
        mid = (start + end) // 2
        for t in trees:
            if t > mid:
                wood += t - mid

        if wood >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(binary_search())

# ClearTime = 2021/06/19 2:23 오후
