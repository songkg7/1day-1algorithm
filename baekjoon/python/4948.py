# 베르트랑 공준
# 기본수학 2, 소수 응용
import math
import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    prime = []
    for num in range(n + 1, 2 * n + 1):
        is_prime = True
        if num == 1:
            continue

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

    print(len(prime))
