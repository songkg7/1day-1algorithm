# 수 정렬하기 2
# 정렬

import sys

N = int(sys.stdin.readline().strip())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers.sort()
for num in numbers:
    print(num)