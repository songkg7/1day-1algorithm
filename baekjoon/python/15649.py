# N과 M
# 백트래킹

from itertools import permutations

N, M = map(int, input().split())
nums = [i + 1 for i in range(N)]
result = permutations(nums, M)
for i in result:
    print(*i)
