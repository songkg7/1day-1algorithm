# 숫자 카드 2
# Binary search
# 2021/06/15 7:24 오전

# 정렬이 되면 같은 숫자는 모여있으므로, 다른 숫자가 나올 때까지 세면 되지 않을까

import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().rstrip().split()))

n = Counter(cards)
for num in target:
    print(n[num] if num in n else 0, end=' ')

# ClearTime = 2021/06/15 8:01 오전
