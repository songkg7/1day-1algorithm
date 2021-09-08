# TITLE: IOIOI
# CATEGORY: 문자열
# DATE: 2021/08/23 7:55 오후

# 찾으면 인덱스를 2 만큼 이동 -1 나올 때까지

N = int(input())
M = int(input())
S = input()

count = 0
answer = 0
stack = []

for i in range(M):
    if S[i] == 'I':
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i - 1] == 2:
        count += 1
    else:
        count = 0

    if count >= N:
        answer += 1

print(answer)

# ClearTime = 2021/08/23 8:17 오후 - 50%
