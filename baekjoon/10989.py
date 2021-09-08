# 수 정렬하기 3
# 정렬

import sys

N = int(input())

check_list = [0] * 10001

for _ in range(N):
    input_num = int(sys.stdin.readline().strip())
    check_list[input_num] += 1

for i in range(10001):
    if check_list[i] != 0:
        for _ in range(check_list[i]):
            print(i)
