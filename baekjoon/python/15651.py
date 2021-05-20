# N과 M (3)
# 백트래킹

from itertools import product

N, M = map(int, input().split())

nums = [i + 1 for i in range(N)]

for num in product(nums, repeat=M):
    print(*num)
