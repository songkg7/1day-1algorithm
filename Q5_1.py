n = int(input())
delay = list(map(int, input().split()))
delay.sort()

sum = 0
for i in range(n):
    sum += delay[i] * (n - i)

print(sum)

# 1
# 1 + 2
# 1 + 2 + 3
# 1 + 2 + 3 + 3
# 1 + 2 + 3 + 3 + 4