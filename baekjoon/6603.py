# TITLE: 로또
# CATEGORY: 수학
# DATE: 2021/10/05 12:55 오후

from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    k = nums[0]
    s = nums[1:k + 1]
    for v in combinations(s, 6):
        print(*v)

    if nums[0] == 0:
        break

    print()

# ClearTime = 2021/10/05 1:04 오후
