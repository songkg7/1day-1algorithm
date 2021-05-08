# 골드바흐의 추측
# 기본수학 2
# 소수 응용

# n보다 작은 소수를 모두 구한 뒤, 그 소수들 중 더해서 n이 되는 것을 찾는다.
# n에서 소수 prime을 빼고 나온 나머지가 n보다 작은 소수 안에 있는지 확인하고 있다면 prime과 나머지를 리턴
import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    prime = []
    result = []
    for num in range(2, n + 1):  # 범위
        is_prime = True
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

    for num in prime:
        if prime.count(n - num) != 0:
            result.append([num, n - num])

    answer = []
    x = n
    for i in result:
        if abs(i[0] - i[1]) < x:
            x = abs(i[0] - i[1])
            answer = [i[0], i[1]]

    print(f'{answer[0]} {answer[-1]}')
