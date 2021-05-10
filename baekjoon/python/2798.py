# 블랙잭
# 브루트포스

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = []
candidates = combinations(cards, 3)
for candidate in candidates:
    if sum(candidate) <= m:
        result.append(sum(candidate))

print(max(result))
