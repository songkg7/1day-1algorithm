# 링
# 정수론 및 조합론

from fractions import Fraction

N = int(input())
r_list = list(map(int, input().split()))

A = r_list[0]
for B in r_list[1:]:
    fraction = Fraction(A, B)
    print(f'{fraction.numerator}/{fraction.denominator}')
