# 좌표 압축
# 정렬

# FIXME: 시간초과

import sys

N = int(sys.stdin.readline().strip())

position = list(map(int, sys.stdin.readline().strip().split()))
encoder = sorted(set(position))

for i in position:
    print(encoder.index(i), end=' ')
