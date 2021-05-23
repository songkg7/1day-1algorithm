# 검문
# 정수론 및 조합론

# nums 의 최대공약수 다음 숫자부터 검사한다. 최대공약수는 반드시 answer 에 포함된다.
# a, b, c 가 nums 의 요소일 경우,
# b - a, c - b 의 최대공약수의 약수가 정답
# 약수는 제곱근까지만 검사한다.


import math

N = int(input())
nums = sorted([int(input()) for _ in range(N)])

diff = []
for i in range(len(nums) - 1):
    diff.append(nums[i + 1] - nums[i])

gcd = math.gcd(*diff)

factor = [gcd]
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        factor.append(i)
        factor.append(gcd // i)

factor = sorted(set(factor))

print(*factor)
