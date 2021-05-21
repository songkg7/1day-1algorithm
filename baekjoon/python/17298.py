# 오큰수
# 스택

# TODO: 다시 풀기

from collections import deque

N = int(input())

seq = list(map(int, input().split()))

oh_big = [-1] * N
stack = deque()

for i in range(N):
    while stack and stack[-1][0] < seq[i]:
        tmp, idx = stack.pop()
        oh_big[idx] = seq[i]
    stack.append([seq[i], i])

print(*oh_big)
