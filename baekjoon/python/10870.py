# 피보나치 수 5
# 재귀함수

n = int(input())


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(n))
