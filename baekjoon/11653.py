# 소인수분해
# 기본수학 2

# 생각 과정
# n을 2부터 순차적으로 나눠보면서 나머지가 0일 경우, i의 값을 배열(answer)에 넣는다.
# n // i 의 몫을 n으로 한 후 다시 2부터 순차적으로 검사해나간다.
# 더 이상 나누어지지 않는다면 n을 배열에 넣고 루프문을 탈출한다.

# n이 소수인지? => 소수라면 소인수분해가 안되므로 자기 자신을 바로 출력해야한다.

# n의 제곱근까지만 검사해본다.

# 한줄씩 출력하는거라 답을 배열에 넣고 다시 출력할 필요없이 바로 출력해도 된다.
import math

n = int(input())

i = 2
while i ** 2 <= n:  # 굳이 n까지 갈 필요없이 i의 제곱까지만 검사해도 된다. int(math.sqrt(n))도 가능
    if n % i == 0:
        print(i)
        n //= i
    else:
        i += 1

if n != 1:
    print(n)

# if answer:
#     for num in answer:
#         print(num)

# 11653
# import sys
# # input = sys.stdin.readline
# print = sys.stdout.write
#
# N = int(input())
# prime = 2
# while prime ** 2 <= N:
#     if N % prime == 0:
#         N //= prime
#         print(str(prime) + "\n")
#     else:
#         prime += 1
#
# if N != 1:
#     print(str(N))
