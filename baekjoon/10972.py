# TITLE: 다음 순열
# CATEGORY: 조합론
# DATE: 2021/09/10 9:10 오후

# TIME OVER
# from itertools import permutations
#
# N = int(input())
# nums = list(map(int, input().split()))
# sort_nums = sorted(nums)
#
# result = list(permutations(sort_nums, N))
#
# for i in range(len(result)):
#     if tuple(nums) == result[i]:
#         if i == len(result) - 1:
#             print(-1)
#             break
#         print(*result[i + 1])

# NOTE: next permutation algorithm

N = int(input())
nums = list(map(int, input().split()))
x = 0

for i in range(N - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        x = i - 1
        break

for i in range(N - 1, 0, -1):
    if nums[x] < nums[i]:
        nums[x], nums[i] = nums[i], nums[x]
        nums = nums[:x + 1] + sorted(nums[x + 1:])
        print(*nums)
        exit()
print(-1)
