# TITLE: 문자열 집합
# CATEGORY: 문자열
# DATE: 2021/08/14 1:04 오후

N, M = map(int, input().split())
s = set([input() for _ in range(N)])
check = [input() for _ in range(M)]

count = 0
for word in check:
    if word in s:
        count += 1

print(count)

# ClearTime = 2021/08/14 1:20 오후
