#
# 완전탐색
# 2021/06/25 4:07 오후

# 한 자리 숫자를 먼저 판별

from itertools import permutations
import math

numbers = "123425"


# 소수 검사
def is_prime(n):
    if n in (0, 1):
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()

    # 한자리 판별
    for i in numbers:
        if is_prime(int(i)):
            answer.add(int(i))

    # 여러 자리수 판별
    for i in range(2, len(numbers) + 1):
        nums = set(map(lambda x: int(''.join(x)), permutations(numbers, i)))

        for num in nums:
            if is_prime(num):
                answer.add(num)

    return len(answer)


print(solution(numbers))

# ClearTime = 2021/06/25 4:32 오후
