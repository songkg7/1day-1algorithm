# X보다 작은 수
# for
# 2021/06/06 5:07 오후

N, X = map(int, input().split())
A = list(map(int, input().split()))

result = filter(lambda x: x < X, A)

print(*result)

# ClearTime = 2021/06/06 5:10 오후
