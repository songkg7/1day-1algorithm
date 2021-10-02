# TITLE: 에라토스테네스의 체
# CATEGORY: 수학
# DATE: 2021/09/30 8:27 오후

# TODO: 다시 풀기

N, K = map(int, input().split())

nums = [False for _ in range(N + 2)]
count = 0

for i in range(2, N + 1):
    if not nums[i]:
        for j in range(i, N + 1, i):
            if not nums[j]:
                nums[j] = True
                count += 1

                if count == K:
                    print(j)
                    break

# ClearTime = 2021/09/30 9:23 오후
