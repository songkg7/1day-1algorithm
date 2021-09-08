# 좌표 압축
# 정렬

import sys

N = int(sys.stdin.readline().strip())

position = list(map(int, sys.stdin.readline().strip().split()))
encoder = sorted(set(position))

dic = {encoder[i]: i for i in range(len(encoder))}

result = [dic[n] for n in position]
print(*result)
