# 분해합
# 브루트포스


def generate(number):
    for s in str(number):
        number += int(s)
    return number


N = int(input())
for num in range(N):
    if generate(num) == N:
        print(num)
        break
    if num == N - 1:
        print(0)
