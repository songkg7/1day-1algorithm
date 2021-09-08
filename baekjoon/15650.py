# N과 M (2)
# 백트래킹

from itertools import combinations

N, M = map(int, input().split())
nums = [i + 1 for i in range(N)]
result = combinations(nums, M)
for i in result:
    print(*i)