# 소수
# 기본수학 2

# 소수를 찾아서 리스트에 넣기
# 배열에서 최소값 min() 과 힙 sum() 을 출력한다.
# 단, 배열이 비었을 경우, -1 을 출력한다.
import math

m = int(input())
n = int(input())

prime = []

for num in range(m, n + 1):
    is_prime = True
    if num == 1:
        is_prime = False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime.append(num)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
