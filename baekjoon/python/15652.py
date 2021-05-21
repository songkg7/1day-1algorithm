# N과 M (4)
# 백트래킹

from itertools import combinations_with_replacement

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]

result = combinations_with_replacement(nums, M)

for i in result:
    print(*i)
