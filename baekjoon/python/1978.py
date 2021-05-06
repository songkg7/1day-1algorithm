# 소수 찾기
# 기본수학 2

# 소수는 1과 자신을 제외한 수로는 나누어지지 않는 숫자이다
# 입력된 수의 제곱근을 구해서 그 숫자까지만 전부 체크해보고 하나라도 나눠지는게 있다면 소수가 아니다
# 입력된 수가 소수라면 count 를 1 증가

# FIXME: 분명히 제대로 동작하는데 통과하지 못한다.

import math

N = int(input())

numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    if num == 1:
        continue

    is_prime = True

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print(f'count : {count}')

# print(int(math.sqrt(N)))
