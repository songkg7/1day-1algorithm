import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


n = int(input())
a = list(map(int, input().split()))

count = 0

for x in range(n):
    if is_prime(a[x]):
        count += 1

print(count)
