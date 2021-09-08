# 주유소
# Greedy
# 2021/06/02 12:53 오전

# TODO: 다시 풀기

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_val = price[0]
cost = 0

for i in range(len(distance)):
    if min_val > price[i]:
        min_val = price[i]
    cost += min_val * distance[i]

print(cost)

# ClearTime = 2021/06/02 1:25 오전
