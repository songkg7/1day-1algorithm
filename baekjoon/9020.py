# 골드바흐의 추측
# 기본수학 2
# 소수 응용

# n보다 작은 소수를 모두 구한 뒤, 그 소수들 중 더해서 n이 되는 것을 찾는다.
# n에서 소수 prime을 빼고 나온 나머지가 n보다 작은 소수 안에 있는지 확인하고 있다면 prime과 나머지를 리턴
import math
import sys

T = int(sys.stdin.readline())


def make_prime():
    arr = []

    for number in range(2, 10000 + 1):  # 범위
        is_prime = True
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            arr.append(number)
    return arr


prime = make_prime()

for _ in range(T):
    n = int(sys.stdin.readline())

    result = []
    answer = []
    for i in prime:
        if i > n:
            break
        answer.append(i)

    for num in answer:
        if answer.count(n - num) != 0:  # O(N^2)
            if result.count([n - num, num]) == 0:
                result.append([num, n - num])

    print(" ".join(map(str, result[-1])))
